import { Buffer } from 'node:buffer'
import jwt from 'jsonwebtoken'
import OSS from 'ali-oss';
import { uuidv7 } from 'uuidv7';

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
    const jwtKey = Buffer.from(Netlify.env.get('INTRA_JWT'), 'base64');
    let rootJson = {};
    try {
        rootJson = jwt.verify(await request.text(), jwtKey, {maxAge: '10s'});
    } catch (e) {
        if (e instanceof jwt.TokenExpiredError) {
            return new Response('Token expired', {status: 401});
        } else {
            throw e;    // unexpected
        }
    }

    const date = new Date();
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