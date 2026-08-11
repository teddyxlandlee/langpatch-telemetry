# Telemetry Analysis Report (2026/07/31 – 2026/08/12)

**Posted by:** teddyxlandlee  
**Date:** 2026-08-12  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/0861e461258233422a2a2881cdf8d2fa)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **July 31, 2026 and August 12, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).

## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 216,863  
  During this 12-day period, a total of **216,863** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (21 days, 298,717 records, ~14,225/day), this period's daily average (~18,072/day) shows an **increase of approximately 27%** . This increase is likely due to the successful recording of schema v3 telemetry (see below) and continued version upgrades that may have reset session counters.

- **Schema version distribution:**
  - `schema_version 2`: **169,241** (78.0%)
  - `schema_version 3`: **47,622** (22.0%)

  > **Important Note on Schema v3:** Version **3.8.15** introduced a new telemetry schema (`schema_version 3`) which adds an additional collection item: the number of registered patches. The middleware issue mentioned in the previous report has been resolved, so this period includes schema v3 data for the first time. This allows us to analyze mod integrations (see Section 6).

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).

## 2. Mod Version Distribution

| Version | User Count | Share |
|---------|------------|-------|
| **3.8.13** | **76,750** | **35.4%** |
| **3.8.10** | **51,759** | **23.9%** |
| **3.8.11** | **33,038** | **15.2%** |
| **3.8.17** | **21,908** | **10.1%** |
| **3.8.15** | **19,665** | **9.1%** |
| 3.8.14 | 6,667 | 3.1% |
| (empty) | 2,904 | 1.3% |
| 3.8.16 | 2,219 | 1.0% |
| 3.8.18 | 1,923 | 0.9% |
| 3.8.12 | 30 | <0.1% |

- **3.8.13 remains the dominant version** at **35.4%**, though its share has declined from 49.3% in the previous period, reflecting the growing diversity of versions.
- **3.8.10** has dropped to **23.9%**, continuing its decline.
- **3.8.17** and **3.8.18** have emerged, with 3.8.17 at **10.1%** and 3.8.18 at **0.9%** .
- **3.8.15** now appears with **9.1%** , thanks to the schema v3 fix.

## 3. Minecraft Version Distribution

| Game Version | User Count | Share |
|--------------|------------|-------|
| **1.21.1** | **90,556** | **41.8%** |
| **1.20.1** | **87,871** | **40.5%** |
| 26.2 | 15,445 | 7.1% |
| 1.21.11 | 12,003 | 5.5% |
| 26.1.2 | 5,970 | 2.8% |
| 1.12.2 | 910 | 0.4% |
| 1.20.2 | 626 | 0.3% |
| 1.21.10 | 622 | 0.3% |
| 1.21.8 | 397 | 0.2% |
| 26.1 | 365 | 0.2% |
| Others | 2,198 | 1.0% |

- **1.21.1 remains the leading game version** at **41.8%**, narrowly ahead of 1.20.1 (40.5%).
- **1.20.1** has stabilized around **40.5%** , showing a slower decline compared to previous periods.
- The “new scheme” versions (26.x) collectively account for **~10.1%** , up from ~7.1% in the previous period, indicating growing adoption.
- **1.21.11** holds at **5.5%**.

## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Fabric** | **96,932** | **44.7%** |
| **Forge** | **89,619** | **41.3%** |
| NeoForge | 30,253 | 13.9% |
| Quilt | 59 | <0.1% |

- **Fabric remains the largest platform** at **44.7%** , though its lead over Forge has narrowed slightly.
- **Forge** holds at **41.3%** , showing resilience.
- **NeoForge** has grown to **13.9%** , its highest share yet.

## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region | User Count | Share |
|----------------|------------|-------|
| **China Mainland** | **110,982** | **51.2%** |
| United States | 23,195 | 10.7% |
| France | 17,081 | 7.9% |
| Russia | 6,737 | 3.1% |
| Brazil | 5,329 | 2.5% |
| Germany | 4,596 | 2.1% |
| United Kingdom | 3,115 | 1.4% |
| Canada | 2,885 | 1.3% |
| Vietnam | 2,734 | 1.3% |
| Poland | 2,024 | 0.9% |

- **China Mainland remains the largest user base** at **51.2%** , but its share has decreased from ~70% in the previous period, indicating a more geographically diverse user base.
- The report covers users from **over 200 countries/regions**, demonstrating global reach.

> **Note:** Geographic distribution data is estimated based on IP geolocation and may not be 100% accurate.

## 6. Patch Count Analysis (Schema v3)

Schema v3 introduced a new metric: `patch_count`. The mod itself registers 2 patches (enchantment and potion). A patch count of 3 or more indicates that other mods have integrated with Enchantment Level Language Patch via its API.

- **Total schema v3 records:** 47,622
- **Patch count distribution:**
  - `patch_count = 2`: **47,201** (99.1%)
  - `patch_count = 3`: **421** (0.9%)

**Key Findings:**
- The vast majority of schema v3 clients (99.1%) use the default 2 patches, indicating that most users run the mod standalone.
- **421 records (0.9%) show 3 or more patches**, confirming that at least some other mods are actively integrating with Enchantment Level Language Patch. This is a positive sign for the mod's ecosystem extensibility.

## 7. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform | Game Version | User Count | Description |
|----------|--------------|------------|-------------|
| **Forge** | **1.20.1** | **85,964** | **Still the largest single combination** |
| Fabric | 1.21.1 | 63,061 | Leading modern combination |
| NeoForge | 1.21.1 | 27,461 | Strong presence on latest versions |
| Fabric | 26.2 | 12,956 | Growing adoption on new scheme |
| Fabric | 1.21.11 | 11,343 | Solid presence on latest release |

- The combination of **Forge + 1.20.1** remains the single largest configuration, representing **39.6%** of all user sessions, though down from 39.9% in the previous period.
- **Fabric + 1.21.1** is now the second-largest pair with 63,061 users.
- **NeoForge** has established a strong presence on **1.21.1** with 27,461 users.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.13** | **Fabric** | **1.21.1** | **59,694** |
| **3.8.10** | **Forge** | **1.20.1** | **42,315** |
| 3.8.11 | Forge | 1.20.1 | 31,811 |
| 3.8.10 | NeoForge | 1.21.1 | 8,343 |
| 3.8.15 | NeoForge | 1.21.1 | 5,874 |
| 3.8.14 | NeoForge | 1.21.1 | 5,418 |

- **3.8.13 + Fabric + 1.21.1** remains the most popular configuration with nearly **60,000** users.
- **3.8.10 + Forge + 1.20.1** remains the second-largest configuration with over **42,000** users.
- **3.8.15** and **3.8.14** show notable presence on NeoForge + 1.21.1, indicating early adoption of newer versions on modern platforms.

## 8. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.13 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://privacy.ellp.mods.hixland.com/privacy) for the latest terms.

## 9. Summary & Outlook

During this telemetry period (July 31 – August 12, 2026), Enchantment Level Language Patch has demonstrated continued ecosystem evolution:

- **Data Volume:** Total records reached **216,863** over 12 days. The daily average increased by ~27% compared to the previous period, indicating improved data collection and possibly higher user engagement.

- **Version Diversity:** **3.8.13** remains the most used version (35.4%), but newer versions like **3.8.17** (10.1%) and **3.8.18** (0.9%) are gaining traction. **3.8.15** now appears with 9.1% thanks to the schema v3 fix.

- **Game Version Shift:** **1.21.1** (41.8%) remains the leading game version, closely followed by **1.20.1** (40.5%). The new scheme (26.x) now accounts for ~10.1% of users, showing steady adoption.

- **Platform Realignment:** **Fabric** (44.7%) retains its lead over **Forge** (41.3%), while **NeoForge** grows to 13.9%, its highest share yet.

- **Geographic Diversification:** **China Mainland** still leads at 51.2%, but its share has decreased, reflecting a more global user base.

- **Ecosystem Health:** The introduction of schema v3 and the patch count metric reveals that **0.9% of schema v3 users have integrations with other mods**, indicating a healthy and extensible ecosystem.

- **Future Outlook:** With the successful recording of schema v3 data, future reports will provide deeper insights into mod integrations. Users are encouraged to keep their mod updated to the latest version to benefit from improvements and contribute to telemetry.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-08-12