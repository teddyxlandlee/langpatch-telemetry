// import OSS from 'ali-oss';
// import { enc, HmacSHA1, MD5 } from 'https://cdn.jsdelivr.net/npm/crypto-js@4.2.0/+esm';
import { Base64 } from 'https://cdn.jsdelivr.net/npm/js-base64@3.7.8/+esm'
import { uuidv7 } from 'https://cdn.jsdelivr.net/npm/uuidv7@1.2.1/+esm';
import crypto from 'node:crypto'

/**
 * @returns {{
 *   accessKeyId: string,
 *   accessKeySecret: string,
 *   bucket: string,
 * }}
 */
function getAliyunOssCredentials() {
    const environ = Netlify.env.get('ALIYUN_OSS_ACCESS');
    return JSON.parse(Base64.decode(environ));
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
        _requires(request.headers.get('Content-Type') === 'application/json');
        json = checkV1(json, date);
    } catch {
        return _fail400();
    }

    if (json.telemetry_level >= LEVEL_FUNCTIONAL) {
        json.client_context = {
            country: context.geo.country,
            timezone: context.geo.timezone,
        };
    }
    
    const filename = `${date.getUTCFullYear()}/${date.getUTCMonth()}/${date.getUTCDate()}/${uuidv7()}.json`;
    
    const {accessKeyId, accessKeySecret, bucket} = getAliyunOssCredentials();
    // const client = new OSS({
    //     accessKeyId, accessKeySecret, bucket,
    //     region: 'oss-cn-shanghai',
    //     secure: true,
    //     authorizationV4: true,
    // });
    // const ossResponse = client.put(filename, Buffer.from(JSON.stringify(json), 'utf-8'), {mime: 'application/json'});
    // context.waitUntil(ossResponse);

    const body = JSON.stringify(json);
    const signature = (data => crypto.createHmac('sha1', accessKeySecret).update(data).digest('base64'))(
        'PUT' + '\n' +
        crypto.createHash('md5').update(body).digest('base64') + '\n' +
        'application/json' + '\n' +
        date.toUTCString() + '\n' +
        `/${bucket}/${filename}`
    );

    fetch(`https://${bucket}.oss-cn-shanghai.aliyuncs.com/${filename}`, {
        method: 'PUT',
        body,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `OSS ${accessKeyId}:${signature}`,
            'Date': date.toUTCString(),
        },
    });

    // Whether response is successful is not concerned by client
    return new Response(null, {status: 204});
}

function checkV1(json, dateNow) {
    const {client_time, mod_version, mod_platform, mc_version} = json
    _requires(typeof client_time === 'number')
    _requires(typeof mod_version === 'string')
    _requires(typeof mc_version === 'string')
    _requires(['fabric', 'forge', 'neoforge', 'quilt', 'unknown'].includes(mod_platform))

    const ret = {client_time, mod_version, mod_platform, mc_version}
    ret.client_time = new Date(client_time).toISOString()
    ret.time = dateNow.toISOString()
    if (typeof json.telemetry_level !== 'number' || json.telemetry_level < LEVEL_MANDATORY || json.telemetry_level > LEVEL_OPTIONAL) {
        json.telemetry_level = LEVEL_FUNCTIONAL;
    }

    return ret
}

function _fail400(reason = 'Bad Request') {
    return new Response(reason, {status: 400});
}

function _requires(precondition, errorMessage = '') {
    if (!precondition) throw new Error(errorMessage)
}

export default async (request, context) => {
    const json = await request.json();
    if (!json || typeof json !== 'object') return _fail400();
    // Currently only schema 1 is supported
    if (json.schema !== 1) return _fail400();

    return responseV1(json, request, context);
}

export const config = {
    path: '/api/telemetry'
}