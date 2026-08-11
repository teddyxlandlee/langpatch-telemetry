# Telemetry Analysis Report (2026/07/31 – 2026/08/11)

**Posted by:** teddyxlandlee  
**Date:** 2026-08-11  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/6c4c7fc4c798e5719fd2c8dff0b7eb6f)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **July 31, 2026 and August 11, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).

## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 216,863  
  During this 31-day period, a total of **216,863** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (21 days, 298,717 records, ~14,225/day), this period's daily average (~6,996/day) shows a **decrease of approximately 50.8%**. This significant decline is likely attributable to a combination of factors: the natural decay of the reporting user base over time, the ongoing version upgrade cycle, and possibly changes in user opt-in behavior or telemetry session resets.

- **Schema version distribution:**
  - `schema_version 3`: **47,622** (22.0%)
  - `schema_version 2`: **169,241** (78.0%)

  > **Important Note on Schema v3:** Version **3.8.15** and later introduced a new telemetry schema (`schema_version 3`) which adds an additional collection item: the total number of registered patches. This period, schema v3 data was successfully recorded, allowing us to analyze patch counts and mod integrations (see Section 7).

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

- **3.8.13** remains the dominant version at **35.4%**, though its share has decreased from 49.3% in the previous period.
- **3.8.10** has dropped to **23.9%** (from 39.2%), continuing its decline.
- Newer versions **3.8.15, 3.8.16, 3.8.17, and 3.8.18** collectively account for **21.1%**, showing healthy adoption of the latest releases.
- **3.8.17** has emerged as the most popular among the new versions, at **10.1%**.

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

- **1.21.1** remains the leading game version at **41.8%**, though its lead over 1.20.1 has narrowed.
- **1.20.1** holds steady at **40.5%** (previous 40.3%).
- The "new scheme" versions (26.x) collectively account for **~10.4%**, showing continued adoption.
- **1.21.11** has increased slightly to **5.5%** (from 4.6%).

## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Fabric** | **96,932** | **44.7%** |
| **Forge** | **89,619** | **41.3%** |
| NeoForge | 30,253 | 14.0% |
| Quilt | 59 | <0.1% |

- **Fabric** remains the largest platform at **44.7%**, though its share has slightly decreased from 47.1%.
- **Forge** has declined to **41.3%** (from 41.6%).
- **NeoForge** has grown to **14.0%** (from 11.3%), strengthening its position as the third major platform.

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

- **China Mainland** remains the largest user base at **51.2%**, though its share has decreased from ~70% in the previous period.
- **United States** has grown to **10.7%**, and **France** to **7.9%**, indicating a more geographically diverse user base.
- The report covers users from **over 150 countries/regions**, demonstrating continued global reach.

> **Note:** Geographic distribution data is estimated based on IP geolocation and may not be 100% accurate.

## 6. Combined Analysis

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
| **3.8.11** | **Forge** | **1.20.1** | **31,811** |
| 3.8.10 | NeoForge | 1.21.1 | 8,343 |
| 3.8.15 | NeoForge | 1.21.1 | 5,874 |
| 3.8.14 | NeoForge | 1.21.1 | 5,418 |

- **3.8.13 + Fabric + 1.21.1** remains the single most popular configuration with nearly **60,000** users, though its lead has narrowed.
- **3.8.10 + Forge + 1.20.1** remains the second-largest configuration with **42,315** users.
- **3.8.11 + Forge + 1.20.1** has risen to third place with **31,811** users, showing continued reliance on the 1.20.1 platform.
- The data shows a continued bifurcation: existing users staying on Forge + 1.20.1, while newer adopters gravitate toward Fabric/NeoForge + 1.21.1.

## 7. Patch Count Analysis (Schema v3)

With the successful collection of schema v3 data, we can now analyze the `patch_count` metric, which was introduced in schema 3. The mod itself registers **2 patches** (one for enchantments, one for potions). Therefore, a patch count of **3 or more** indicates that other mods are integrating with Enchantment Level Language Patch.

### Distribution of Patch Counts

| Patch Count | User Count | Share |
|-------------|------------|-------|
| **2** | **47,201** | **99.1%** |
| **3** | **421** | **0.9%** |

- The vast majority (99.1%) of schema v3 records report exactly **2 patches**, which is the baseline for the mod itself.
- A small but notable fraction (**0.9%**) report **3 or more patches**, indicating that some users have other mods that integrate with Enchantment Level Language Patch.

### Implications
- The presence of **421 records with 3+ patches** suggests that mod integrations are being used by a small but real subset of the user base.
- This data provides valuable insight into the ecosystem's adoption of integration features and will help guide future development priorities.

## 8. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.13 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://privacy.ellp.mods.hixland.com/privacy) for the latest terms.

## 9. Summary & Outlook

During this telemetry period (July 11 – August 11, 2026), Enchantment Level Language Patch has demonstrated continued ecosystem evolution:

- **Data Volume:** Total records reached **216,863** over 31 days. The decline in daily average compared to the previous period is notable and warrants monitoring in future periods.

- **Version Landscape:** **3.8.13** remains the dominant version at **35.4%**, but the newer versions (3.8.15–3.8.18) collectively account for **21.1%**, showing strong adoption of the latest releases. **3.8.17** has become the most popular among the new versions.

- **Game Version Stability:** **1.21.1** continues to lead at **41.8%**, with **1.20.1** close behind at **40.5%**. The new scheme (26.x) now accounts for ~10.4%.

- **Platform Dynamics:** **Fabric** remains the largest platform at **44.7%**, while **NeoForge** has grown to **14.0%**, indicating a gradual shift toward newer platforms.

- **Geographic Shift:** **China Mainland** remains the largest user base at **51.2%**, but its share has decreased, with **United States** and **France** gaining ground.

- **Patch Count Insights:** The introduction of schema v3 has enabled analysis of mod integrations. The finding that **0.9% of users have 3+ patches** suggests a small but active integration ecosystem.

- **Ecosystem Health:** The continued adoption of newer versions and the growth of NeoForge demonstrate a vibrant, upgrade-oriented ecosystem.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-08-11