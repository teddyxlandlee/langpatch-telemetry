// import OSS from 'https://cdn.jsdelivr.net/npm/ali-oss@6.23.0/+esm';
// import { uuidv7 } from 'https://cdn.jsdelivr.net/npm/uuidv7@1.2.1/+esm';
import { Buffer } from 'node:buffer'
import crypto from 'node:crypto'

const LEVEL_MANDATORY = 0;
const LEVEL_FUNCTIONAL = 1;
const LEVEL_OPTIONAL = 2;

const SCHEMA_VERSION = 2;

/**
 * 
 * @param {object} json 
 * @param {Request} request 
 * @returns {Response}
 */
async function responseV1V2(json, request, context) {
    try {
        _requires(request.headers.get('Content-Type') === 'application/json', 'Content type must be application/json');
        json = checkV1V2(json);
    } catch (e) {
        return _fail400(e.message);
    }

    if (json.telemetry_level >= LEVEL_FUNCTIONAL) {
        json.client_context = {
            country: context.geo.country,
            timezone: context.geo.timezone,
        };
    }
    
    const jwtKey = Buffer.from(Netlify.env.get('INTRA_JWT'), 'base64');
    const jsonBuffer = Buffer.from(JSON.stringify(json), 'utf-8');
    const signature = crypto.createHmac('sha512', jwtKey).update(jsonBuffer).digest('base64');
    const internalRequestPromise = fetch(new URL('/.netlify/functions/telemetry-impl', context.site.url), {
        method: 'POST',
        body: JSON.stringify({data: jsonBuffer.toString('base64'), signature}),
    });
    context.waitUntil(internalRequestPromise);

    // Whether response is successful is not concerned by client
    return new Response(null, {status: 202});
}

function checkV1V2(json) {
    let client_time = json.client_time;
    _requires(typeof client_time === 'number', 'Numeral time required');

    let telemetryLevel = json.telemetry_level;
    if (typeof telemetryLevel !== 'number' || telemetryLevel < LEVEL_MANDATORY || telemetryLevel > LEVEL_OPTIONAL) {
        json.telemetry_level = LEVEL_FUNCTIONAL;
        telemetryLevel = LEVEL_FUNCTIONAL;
    }

    let ret = {schema: json.schema, telemetry_level: telemetryLevel};
    
    if (telemetryLevel >= LEVEL_FUNCTIONAL) {
        const {mod_version, mod_platform, mc_version} = json
        _requires(typeof mod_version === 'string', 'string mod_version required')
        _requires(typeof mc_version === 'string', 'string mc_version required')
        _requires(['fabric', 'forge', 'neoforge', 'quilt', 'unknown'].includes(mod_platform), 'unsupported mod platform')

        ret = {mod_version, mod_platform, mc_version}
    }


    ret.client_time = new Date(client_time).toISOString()
    ret.now = Date.now();   // For proxy validation

    // Also v2 fields
    if (json.schema >= 2) {
        if (telemetryLevel >= LEVEL_FUNCTIONAL) {
            _requires(typeof json.current_hooks === 'object', 'current_hooks object must be present for schema v2, level 1');
            const {enchantment, potion} = json.current_hooks;
            _validateResourceLocation(enchantment, 'enchantment hooks');
            _validateResourceLocation(potion, 'potion hooks');
            ret.current_hooks = {enchantment, potion};
        }
        if (telemetryLevel >= LEVEL_OPTIONAL) {
            _requires(typeof json.current_hooks === 'object', 'all_hooks object must be present for schema v2, level 2')
            const {enchantment, potion} = json.all_hooks;
            _requires(Array.isArray(enchantment), 'all_hooks.enchantment must be array');
            _requires(Array.isArray(potion), 'all_hooks.potion must be array');
            enchantment.forEach((e, idx) => _requires(_validateResourceLocation(e, 'all_hooks.enchantment#' + idx)));
            potion.forEach((e, idx) => _requires(_validateResourceLocation(e, 'all_hooks.potion#' + idx)));
            ret.all_hooks = {enchantment, potion};
        }
    }

    return ret
}

function _fail400(reason = 'Bad Request') {
    return new Response(reason || '', {status: 400});
}

function _requires(precondition, errorMessage = '') {
    if (!precondition) throw new Error(errorMessage)
}

function _validateResourceLocation(field, fieldName = 'Input') {
    _requires(
        typeof field === 'string' && /^([0-9a-z_\-]+:)?[0-9a-z_\-/]+$/.test(field),
        fieldName + ' must be valid resource location'
    );
}

export default async (request, context) => {
    if (request.method !== 'POST') {
        return _fail400("Invalid request method: " + request.method);
    }

    const json = await request.json();
    if (!json || typeof json !== 'object') return _fail400('Not JSON object');
    // Currently only schema 1 & 2 is supported
    if (typeof json.schema !== 'number' || json.schema <= 0 || json.schema > SCHEMA_VERSION) {
        return _fail400('Schema must be 1..' + SCHEMA_VERSION);
    }

    return responseV1V2(json, request, context);
}

export const config = {
    path: '/api/telemetry'
}