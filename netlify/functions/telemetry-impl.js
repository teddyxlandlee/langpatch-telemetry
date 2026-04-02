import { Buffer } from 'node:buffer'
// import jwt from 'jsonwebtoken'
import OSS from 'ali-oss';
import { uuidv7 } from 'uuidv7';
import crypto from 'node:crypto'

/**
 * @returns {{
 *   accessKeyId: string,
 *   accessKeySecret: string,
 *   bucket: string,
 * }}
 */
function getAliyunOssCredentials() {
    const environ = process.env.get('ALIYUN_OSS_ACCESS');
    return JSON.parse(Buffer.from(environ, 'base64').toString('utf-8'));
}


/**
 * @param {Reqeust} request
 * @param {*} context
 * @returns {Response}
 */
export default async (request, context) => {
    if (request.method !== 'POST') {
        return new Response('Invalid request method: ' + request.method, {status: 400});
    }

    const jwtKey = Buffer.from(process.env.get('INTRA_JWT'), 'base64');
    const {data: jsonRaw, signature: jsonSignature} = await request.json();
    const jsonBuffer = Buffer.from(jsonRaw, 'base64');
    const expectedSignature = crypto.createHmac('sha512', jwtKey).update(jsonBuffer).digest('base64');
    if (jsonSignature !== expectedSignature) {
        return new Response('Unauthorized access', {status: 401});
    }

    const json = JSON.parse(jsonBuffer.toString('utf-8'));
    const prevProxyDate = new Date(json.now);
    const date = new Date();
    if (date - prevProxyDate > 10_000) {
        return new Response('Token expired', {status: 408});
    }

    const filename = `${date.getUTCFullYear()}/${date.getUTCMonth()}/${date.getUTCDate()}/${uuidv7()}.json`;
    
    const {accessKeyId, accessKeySecret, bucket} = getAliyunOssCredentials();
    const client = new OSS({
        accessKeyId, accessKeySecret, bucket,
        region: 'oss-cn-shanghai',
        secure: true,
        authorizationV4: true,
    });
    const promise = client.put(filename, Buffer.from(JSON.stringify(rootJson.data)), {
        mime: 'application/json'
    });
    context.waitUntil(promise);
    return new Response(null, {status: 202});
}