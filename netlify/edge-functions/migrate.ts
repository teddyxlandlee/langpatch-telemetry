import { Config, Context, EdgeFunction } from '@netlify/edge-functions'

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

const fun: EdgeFunction = async (request: Request, context: Context) => {
    if (request.method !== 'POST') {
        return new Response('Bad request method', {status: 405})
    }

    if (await isWhitelisted(request)) {
        return new Response('Migrated to ' + MIGRATED_URL, {
            status: 307,    // Temporary Redirect
            headers: {
                // Real redirect target, supported by 3.8.10+
                'Location': MIGRATED_URL,
                'Content-Type': 'text/plain; charset=utf-8',
                // Whitelisted endpoint, used as reverse proxy
                'X-Entrypoint-Redirect': 'https://telemetry2.langpatch.mc.7c7.icu/migrate',
            }
        })
    } else {
        // const { default: legacyFun } = await import('./telemetry.js')
        const { default: legacyFun } = await import ('./migrate-impl.ts')
        return legacyFun(request, context)
    }
}

//noinspection JsUnusedGlobalSymbols
export default fun