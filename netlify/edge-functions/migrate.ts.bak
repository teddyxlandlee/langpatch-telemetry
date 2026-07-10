import type { Config, Context, EdgeFunction } from '@netlify/edge-functions'

//noinspection JsUnusedGlobalSymbols
export const config: Config = {
    path: '/api/telemetry'
}

const ENABLE_REDIRECT: boolean = true

const MIGRATED_URL = Netlify.env.get('MIGRATED_URL') || 'https://url.invalid'

const REDIRECT_VERSION_WHITELIST: readonly string[] = [
    // '3.8.6',
    '3.8.10',
] as const

async function isWhitelisted(request: Request): Promise<boolean> {
    if (!ENABLE_REDIRECT) return false

    try {
        const clone = request.clone()
        const body = await clone.json()
        return body && typeof body === 'object' && REDIRECT_VERSION_WHITELIST.includes(body.mod_version)
    } catch {
        return false
    }
}

const fun: EdgeFunction = async (request: Request, _context: Context) => {
    if (request.method !== 'POST') {
        return new Response('Bad request method', {status: 405})
    }

    if (await isWhitelisted(request)) {
        return new Response('Migrated to ' + MIGRATED_URL, {
            status: 308,    // Permanent Redirect
            headers: {
                // Real redirect target, supported by 3.8.10+
                'Location': MIGRATED_URL,
                'Content-Type': 'text/plain; charset=utf-8',
                // No reverse proxy
            }
        })
    } else {
        return new Response('Legacy versions are no longer supported', {status: 410})
    }
}

//noinspection JsUnusedGlobalSymbols
export default fun