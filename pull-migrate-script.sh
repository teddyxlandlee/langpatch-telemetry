#!/usr/bin/env bash
wget -O ./migrate-impl.ts https://telemetry2.langpatch.mc.7c7.icu/netlify/edge-functions/migrate.ts
sed -i 's/LangPatch-Migrate-Proxy/LangPatch-Migrate-Proxy (v1)/g' ./migrate-impl.ts