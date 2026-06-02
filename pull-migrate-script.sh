#!/usr/bin/env bash
wget -O ./netlify/edge-functions/migrate-impl.ts https://telemetry2.langpatch.mc.7c7.icu/netlify/edge-functions/migrate.ts
sed -i 's/LangPatch-Migrate-Proxy/LangPatch-Migrate-Proxy (v1)/g' ./netlify/edge-functions/migrate-impl.ts
sed -i "s|import jwt from 'jsonwebtoken'|import jwt from 'https://esm.sh/jsonwebtoken'|g" ./netlify/edge-functions/migrate-impl.ts
