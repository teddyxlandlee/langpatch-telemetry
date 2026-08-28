# Telemetry Analysis Report (2026/08/12 – 2026/08/28)

**Posted by:** teddyxlandlee  
**Date:** 2026-08-28  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/6dea83906c52dba81b8bcd4b62157cad)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **August 12, 2026 and August 28, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).

## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 489,896  
  During this 16-day period, a total of **489,896** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (12 days, 216,863 records, ~18,072/day), this period's daily average (~30,619/day) shows a **significant increase of approximately 69%** . This increase is likely due to a combination of factors, including the successful recording of schema v3 telemetry (see below), continued version upgrades that may have reset session counters, and possibly increased user engagement.

- **Schema version distribution:**
  - `schema_version 2`: **399,223** (81.5%)
  - `schema_version 3`: **90,673** (18.5%)

  > **Important Note on Schema v3:** Version **3.8.15** introduced a new telemetry schema (`schema_version 3`) which adds an additional collection item: the number of registered patches. The middleware issue mentioned in the previous report has been resolved, so this period includes schema v3 data for the first time. This allows us to analyze mod integrations (see Section 6).

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).

## 2. Mod Version Distribution

| Version | User Count | Share |
|---------|------------|-------|
| **3.8.11** | **258,803** | **52.8%** |
| **3.8.13** | **90,689** | **18.5%** |
| **3.8.18** | **58,062** | **11.9%** |
| **3.8.10** | **43,433** | **8.9%** |
| **3.8.15** | **20,281** | **4.1%** |
| 3.8.17 | 8,000 | 1.6% |
| 3.8.14 | 6,068 | 1.2% |
| (empty) | 4,182 | 0.9% |
| 3.8.16 | 360 | 0.1% |
| 3.8.12 | 18 | <0.1% |

- **3.8.11 has surged to the dominant version** at **52.8%**, a dramatic increase from 15.2% in the previous period. This suggests a widespread rollout or forced update to this version.
- **3.8.13** has dropped to **18.5%** from 35.4% previously, indicating a migration away from it.
- **3.8.18** has grown significantly to **11.9%** (from 0.9%), showing strong adoption of the latest version.
- **3.8.10** continues to decline to **8.9%**.

## 3. Minecraft Version Distribution

| Game Version | User Count | Share |
|--------------|------------|-------|
| **1.20.1** | **318,345** | **65.0%** |
| **1.21.1** | **118,667** | **24.2%** |
| 26.2 | 21,544 | 4.4% |
| 1.21.11 | 16,175 | 3.3% |
| 26.1.2 | 8,124 | 1.7% |
| 1.12.2 | 1,413 | 0.3% |
| 1.21.10 | 1,180 | 0.2% |
| 1.20.2 | 722 | 0.1% |
| 26.1 | 551 | 0.1% |
| 1.16.5 | 465 | 0.1% |
| Others | 3,890 | 0.8% |

- **1.20.1 has become the leading game version** at **65.0%**, a significant increase from 40.5% in the previous period. This is likely tied to the surge in 3.8.11 usage, which is predominantly on Forge 1.20.1.
- **1.21.1** has dropped to **24.2%** from 41.8%, but remains the second most popular.
- The "new scheme" versions (26.x) collectively account for **~6.2%**, up from ~10.1% in the previous period, but their share has decreased due to the overall growth.
- **1.21.11** holds at **3.3%**.

## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Forge** | **320,741** | **65.5%** |
| **Fabric** | **132,321** | **27.0%** |
| NeoForge | 36,773 | 7.5% |
| Quilt | 51 | <0.1% |
| Legacy Fabric | 6 | <0.1% |
| Ornithes | 4 | <0.1% |

- **Forge has regained a commanding lead** at **65.5%**, up from 41.3% in the previous period. This is a major shift, largely driven by the dominance of 3.8.11 on Forge 1.20.1.
- **Fabric** has dropped to **27.0%** from 44.7%, but remains the second largest platform.
- **NeoForge** has decreased to **7.5%** from 13.9%, possibly due to the popularity of 3.8.11 on other platforms.

## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region | User Count | Share |
|----------------|------------|-------|
| **China Mainland** | **351,317** | **71.7%** |
| United States | 30,566 | 6.2% |
| France | 14,485 | 3.0% |
| Russia | 8,993 | 1.8% |
| Brazil | 8,090 | 1.7% |
| Germany | 7,570 | 1.5% |
| United Kingdom | 4,377 | 0.9% |
| Canada | 4,029 | 0.8% |
| Vietnam | 3,925 | 0.8% |
| Taiwan | 3,760 | 0.8% |

- **China Mainland remains the largest user base** at **71.7%**, a significant increase from 51.2% in the previous period, indicating a strong concentration of users in that region.
- The report covers users from **over 200 countries/regions**, demonstrating global reach.

> **Note:** Geographic distribution data is estimated based on IP geolocation and may not be 100% accurate.

## 6. Patch Count Analysis (Schema v3)

Schema v3 introduced a new metric: `patch_count`. The mod itself registers 2 patches (enchantment and potion). A patch count of 3 or more indicates that other mods have integrated with Enchantment Level Language Patch via its API.

- **Total schema v3 records:** 90,673
- **Patch count distribution:**
  - `patch_count = 2`: **90,535** (99.8%)
  - `patch_count = 3`: **138** (0.2%)

**Key Findings:**
- The vast majority of schema v3 clients (99.8%) use the default 2 patches, indicating that most users run the mod standalone.
- **138 records (0.2%) show 3 or more patches**, confirming that at least some other mods are actively integrating with Enchantment Level Language Patch. This is a positive sign for the mod's ecosystem extensibility.

## 7. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform | Game Version | User Count | Description |
|----------|--------------|------------|-------------|
| **Forge** | **1.20.1** | **316,323** | **Still the largest single combination** |
| Fabric | 1.21.1 | 85,894 | Leading modern combination |
| NeoForge | 1.21.1 | 32,724 | Strong presence on latest versions |
| Fabric | 26.2 | 18,109 | Growing adoption on new scheme |
| Fabric | 1.21.11 | 15,311 | Solid presence on latest release |

- The combination of **Forge + 1.20.1** remains the single largest configuration, representing **64.6%** of all user sessions, up from 39.9% in the previous period.
- **Fabric + 1.21.1** is now the second-largest pair with 85,894 users.
- **NeoForge** has established a strong presence on **1.21.1** with 32,724 users.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.11** | **Forge** | **1.20.1** | **257,345** |
| **3.8.13** | **Fabric** | **1.21.1** | **81,214** |
| 3.8.10 | Forge | 1.20.1 | 36,493 |
| 3.8.18 | Fabric | 26.2 | 13,011 |
| 3.8.18 | NeoForge | 1.21.1 | 12,744 |
| 3.8.18 | Forge | 1.20.1 | 11,017 |

- **3.8.11 + Forge + 1.20.1** is the most popular configuration with over **257,000** users, a massive increase from the previous period.
- **3.8.13 + Fabric + 1.21.1** remains a strong configuration with over **81,000** users.
- **3.8.18** shows notable presence across multiple platforms, indicating early adoption of the latest version.

## 8. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.13 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://privacy.ellp.mods.hixland.com/privacy) for the latest terms.

## 9. Summary & Outlook

During this telemetry period (August 12 – August 28, 2026), Enchantment Level Language Patch has demonstrated significant shifts in its user base:

- **Data Volume:** Total records reached **489,896** over 16 days. The daily average increased by ~69% compared to the previous period, indicating improved data collection and possibly higher user engagement.

- **Version Diversity:** **3.8.11** has become the dominant version (52.8%), while **3.8.18** has grown to 11.9%. **3.8.13** has decreased to 18.5%. The distribution shows a clear migration toward 3.8.11 and the latest 3.8.18.

- **Game Version Shift:** **1.20.1** has surged to 65.0%, while **1.21.1** has dropped to 24.2%. The new scheme (26.x) now accounts for ~6.2% of users, showing steady adoption.

- **Platform Realignment:** **Forge** has regained a dominant lead at 65.5%, while **Fabric** has dropped to 27.0%. **NeoForge** has decreased to 7.5%.

- **Geographic Concentration:** **China Mainland** has increased to 71.7%, indicating a stronger concentration of users in that region.

- **Ecosystem Health:** The introduction of schema v3 and the patch count metric reveals that **0.2% of schema v3 users have integrations with other mods**, indicating a healthy and extensible ecosystem.

- **Future Outlook:** With the successful recording of schema v3 data, future reports will provide deeper insights into mod integrations. Users are encouraged to keep their mod updated to the latest version to benefit from improvements and contribute to telemetry.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-08-28