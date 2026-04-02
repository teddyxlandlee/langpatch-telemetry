import OSS from 'https://cdn.jsdelivr.net/npm/ali-oss@6.23.0/+esm';
// import { enc, HmacSHA1, MD5 } from 'https://cdn.jsdelivr.net/npm/crypto-js@4.2.0/+esm';
import { uuidv7 } from 'https://cdn.jsdelivr.net/npm/uuidv7@1.2.1/+esm';
import crypto from 'node:crypto'
import { Buffer } from 'node:buffer'

/**
 * @returns {{
 *   accessKeyId: string,
 *   accessKeySecret: string,
 *   bucket: string,
 * }}
 */
function getAliyunOssCredentials() {
    const environ = Netlify.env.get('ALIYUN_OSS_ACCESS');
    return JSON.parse(Buffer.from(environ, 'base64').toString('utf-8'));
}

const LEVEL_MANDATORY = 0;
const LEVEL_FUNCTIONAL = 1;
const LEVEL_OPTIONAL = 2;

/**
 * 
 * @param {object} json 
 * @param {Request} request 
 * @returns {Response}
 */
async function responseV1(json, request, context) {
    const date = new Date();
    try {
        _requires(request.headers.get('Content-Type') === 'application/json', 'Content type must be application/json');
        json = checkV1(json, date);
    } catch (e) {
        return _fail400(e.message);
    }

    if (json.telemetry_level >= LEVEL_FUNCTIONAL) {
        json.client_context = {
            country: context.geo.country,
            timezone: context.geo.timezone,
        };
    }
    
    const filename = `${date.getUTCFullYear()}/${date.getUTCMonth()}/${date.getUTCDate()}/${uuidv7()}.json`;
    
    const {accessKeyId, accessKeySecret, bucket} = getAliyunOssCredentials();
    const client = new OSS({
        accessKeyId, accessKeySecret, bucket,
        region: 'oss-cn-shanghai',
        secure: true,
        authorizationV4: true,
    });
    const ossResponse = client.put(filename, Buffer.from(JSON.stringify(json), 'utf-8'), {mime: 'application/json'});
    context.waitUntil(ossResponse.then(console.log));   // DEBUG

    // Whether response is successful is not concerned by client
    return new Response(null, {status: 204});
}

function checkV1(json, dateNow) {
    let client_time = json.client_time;
    _requires(typeof client_time === 'number', 'Numeral time required');

    let telemetryLevel = json.telemetry_level;
    if (typeof telemetryLevel !== 'number' || telemetryLevel < LEVEL_MANDATORY || telemetryLevel > LEVEL_OPTIONAL) {
        json.telemetry_level = LEVEL_FUNCTIONAL;
        telemetryLevel = LEVEL_FUNCTIONAL;
    }

    let ret = {};
    
    if (telemetryLevel >= LEVEL_FUNCTIONAL) {
        const {mod_version, mod_platform, mc_version} = json
        _requires(typeof mod_version === 'string', 'string mod_version required')
        _requires(typeof mc_version === 'string', 'string mc_version required')
        _requires(['fabric', 'forge', 'neoforge', 'quilt', 'unknown'].includes(mod_platform), 'unsupported mod platform')

        ret = {mod_version, mod_platform, mc_version}
    }


    ret.client_time = new Date(client_time).toISOString()
    ret.time = dateNow.toISOString()

    return ret
}

function _fail400(reason = 'Bad Request') {
    return new Response(reason || '', {status: 400});
}

function _requires(precondition, errorMessage = '') {
    if (!precondition) throw new Error(errorMessage)
}

export default async (request, context) => {
    const json = await request.json();
    if (!json || typeof json !== 'object') return _fail400('Not JSON object');
    // Currently only schema 1 is supported
    if (json.schema !== 1) return _fail400('Schema must be 1');

    return responseV1(json, request, context);
}

export const config = {
    path: '/api/telemetry'
}