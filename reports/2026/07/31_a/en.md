# Telemetry Analysis Report (2026/07/10 – 2026/07/31)

**Posted by:** teddyxlandlee  
**Date:** 2026-07-31  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/05d815cb1df119c39594d2cdb30d676e)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **July 10, 2026 and July 31, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).


## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 298,717  
  During this 21-day period, a total of **298,717** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (21 days, 349,415 records, ~16,639/day), this period’s daily average (~14,225/day) shows a **decrease of approximately 14.5%** . This decline is likely attributable to the natural decay of the reporting user base over time, as well as the continued version upgrade cycle—many users have already migrated from 3.8.10 to 3.8.13/3.8.14 (see Section 2), which may have reset telemetry session counters for some clients.

- **Schema version distribution:**
  - `schema_version 2`: **298,717** (100%)

  > **Important Note on Schema v3:** Version **3.8.15** introduced a new telemetry schema (`schema_version 3`) which adds an additional collection item: the total number of registered hooks. However, due to an oversight on my part, telemetry data using schema v3 was intercepted by a misconfigured middleware rule and was not recorded during this period. As a result, all records in this report are `schema_version 2`, and **3.8.15 does not appear in the version distribution below**.

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).


## 2. Mod Version Distribution

| Version | User Count | Share |
|---------|------------|-------|
| **3.8.13** | **147,224** | **49.3%** |
| **3.8.10** | **117,053** | **39.2%** |
| **3.8.14** | **17,187** | **5.8%** |
| 3.8.11 | 14,837 | 5.0% |
| (empty) | 2,368 | 0.8% |
| 3.8.12 | 48 | <0.1% |

> *Note: Version 3.8.15 is absent from the table above due to the schema v3 interception issue noted in Section 1.*

- **3.8.13 has overtaken 3.8.10 as the dominant version** at **49.3%**, marking a major milestone in the mod's version transition.
- **3.8.10** has declined to **39.2%** (from 54.3% in the previous period), continuing its steady downward trend.
- **3.8.14** has grown substantially to **5.8%** (up from 1.2%), showing healthy adoption of the newest release.
- **3.8.11** has increased slightly to **5.0%** (up from 4.2%), possibly due to users on older versions upgrading incrementally.


## 3. Minecraft Version Distribution

| Game Version | User Count | Share |
|--------------|------------|-------|
| **1.21.1** | **138,677** | **46.4%** |
| **1.20.1** | **120,462** | **40.3%** |
| 1.21.11 | 13,851 | 4.6% |
| 26.2 | 12,227 | 4.1% |
| 26.1.2 | 7,567 | 2.5% |
| 1.12.2 | 1,496 | 0.5% |
| 26.1 | 771 | 0.3% |
| 1.21.10 | 646 | 0.2% |
| 1.16.5 | 488 | 0.2% |
| 1.19.2 | 372 | 0.1% |
| Others | 2,162 | 0.7% |

- **1.21.1 has become the leading game version** at **46.4%**, surpassing 1.20.1 for the first time in this reporting history.
- **1.20.1** has dropped to **40.3%** (from 48.3%), reflecting the ongoing migration toward newer versions.
- The “new scheme” versions (26.x) collectively account for **~7.1%**, showing continued but slightly slower adoption of newer release trains.
- **1.21.11** holds at **4.6%** (down from 5.8%).


## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Fabric** | **140,651** | **47.1%** |
| **Forge** | **124,195** | **41.6%** |
| NeoForge | 33,790 | 11.3% |
| Quilt | 75 | <0.1% |
| Legacy-Fabric | 6 | <0.1% |

- **Fabric has overtaken Forge as the largest platform** at **47.1%**, a significant shift from the previous period when Forge led at 49.3%.
- **Forge** has declined to **41.6%** (from 49.3%), losing its long-held top position.
- **NeoForge** remains stable at **11.3%** (down slightly from 11.6%), continuing its presence as the third major platform.


## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region | User Count | Share |
|----------------|------------|-------|
| **China Mainland** | **208,500** | **69.8%** |
| United States | 17,923 | 6.0% |
| Russia | 8,364 | 2.8% |
| France | 7,767 | 2.6% |
| Germany | 4,481 | 1.5% |
| United Kingdom | 2,688 | 0.9% |
| Japan | 2,390 | 0.8% |
| Brazil | 2,390 | 0.8% |
| Canada | 2,390 | 0.8% |
| Taiwan | 2,091 | 0.7% |

- **China Mainland remains the largest user base** at **69.8%**, stable compared to the previous period (69.8%).
- The report covers users from **over 150 countries/regions**, demonstrating continued global reach.

> **Note:** Geographic distribution data is estimated based on IP geolocation and may not be 100% accurate.


## 6. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform | Game Version | User Count | Description |
|----------|--------------|------------|-------------|
| **Forge** | **1.20.1** | **119,123** | **Still the largest single combination** |
| Fabric | 1.21.1 | 107,276 | Leading modern combination |
| NeoForge | 1.21.1 | 31,305 | Strong presence on latest versions |
| Fabric | 1.21.11 | 13,307 | Solid presence on latest release |
| Fabric | 26.2 | 10,108 | Growing adoption on new scheme |

- The combination of **Forge + 1.20.1** remains the single largest configuration, representing **39.9%** of all user sessions, though down significantly from 47.5% in the previous period.
- **Fabric + 1.21.1** is now the second-largest pair with 107,276 users, closing the gap with the top combination.
- **NeoForge** has established a strong presence on **1.21.1** with 31,305 users.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.13** | **Fabric** | **1.21.1** | **104,495** |
| **3.8.10** | **Forge** | **1.20.1** | **100,085** |
| 3.8.10 | NeoForge | 1.21.1 | 13,462 |
| 3.8.11 | Forge | 1.20.1 | 10,952 |
| 3.8.13 | Fabric | 1.21.11 | 9,729 |
| 3.8.13 | NeoForge | 1.21.1 | 9,305 |

- **3.8.13 + Fabric + 1.21.1** has become the single most popular configuration with over **104,000** users, surpassing the long-dominant 3.8.10 + Forge + 1.20.1 combination.
- **3.8.10 + Forge + 1.20.1** remains the second-largest configuration with just over **100,000** users.
- The data shows a clear bifurcation trend: existing users staying on 3.8.10 + Forge + 1.20.1, while newer adopters and upgraders gravitate toward 3.8.13 + Fabric/NeoForge + 1.21.1.
- **3.8.14** is beginning to appear across multiple platform-version combinations, with notable presence on NeoForge + 1.21.1 (8,109 users) and Fabric + 26.2 (1,949 users).


## 7. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.13 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://privacy.ellp.mods.hixland.com/privacy) for the latest terms.


## 8. Summary & Outlook

During this telemetry period (July 10 – July 31, 2026), Enchantment Level Language Patch has demonstrated significant ecosystem evolution:

- **Data Volume:** Total records reached **298,717** over 21 days. The decline in daily average compared to the previous period reflects natural user base decay over time and the continued version upgrade cycle that may have reset session counters.

- **Version Revolution:** **3.8.13** has achieved a landmark **49.3%** adoption, officially surpassing 3.8.10 (39.2%) to become the dominant version—a historic milestone for the mod. **3.8.14** (5.8%) continues to gain traction.

- **Game Version Shift:** **1.21.1** has overtaken **1.20.1** (46.4% vs. 40.3%) as the leading game version for the first time, marking a major ecosystem transition. The new scheme (26.x) now accounts for ~7.1% of users.

- **Platform Realignment:** **Fabric** (47.1%) has overtaken **Forge** (41.6%) as the largest platform for the first time, reflecting a significant shift in the mod's user base composition. **NeoForge** (11.3%) remains stable.

- **Geographic Stability:** **China Mainland** remains the largest user base at ~70%, with global distribution remaining consistent.

- **Ecosystem Health:** The continued adoption of **3.8.13** (49.3%) and the growth of **3.8.14** (5.8%) demonstrate a vibrant, upgrade-oriented ecosystem with strong user engagement.

- **Note on 3.8.15:** Although version 3.8.15 was released during this period, its telemetry data was not recorded due to the schema v3 interception issue mentioned in Section 1. Users are encouraged to upgrade and future reports will include 3.8.15 data once the issue is resolved.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-07-31