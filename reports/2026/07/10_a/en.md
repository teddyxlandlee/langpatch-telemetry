# Telemetry Analysis Report (2026/06/19 – 2026/07/10)

**Posted by:** teddyxlandlee  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/9f128cbd8dad01a409fc1ab28dfd54f3)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **June 19, 2026 and July 10, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).


## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 349,415  
  During this 21-day period, a total of **349,415** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (7 days, 213,562 records, ~30,509/day), this period’s daily average (~16,639/day) shows a **decrease of approximately 45.5%** . This decline is likely attributable to the natural decay of the reporting user base over the extended collection window, as well as the rapid version upgrade cycle during this period—many users upgraded from 3.8.10 to 3.8.13 (see Section 2), which may have reset telemetry session counters for some clients.

- **Schema version distribution:**
  - `schema_version 2`: **349,141** (99.9%)
  - `schema_version 1`: **274** (0.1%)

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).


## 2. Mod Version Distribution

| Version | User Count | Share |
|---------|------------|-------|
| **3.8.10** | **189,749** | **54.3%** |
| **3.8.13** | **133,285** | **38.1%** |
| 3.8.11 | 14,792 | 4.2% |
| 3.8.14 | 4,080 | 1.2% |
| (empty) | 3,858 | 1.1% |
| 3.8.6 | 1,585 | 0.5% |
| 3.8.4 | 1,341 | 0.4% |
| 3.8.5 | 239 | 0.1% |
| 3.8.1 | 234 | 0.1% |
| 3.8.12 | 108 | <0.1% |
| 3.8.2 | 107 | <0.1% |
| 3.8.0 | 37 | <0.1% |

- **3.8.10 remains the dominant version** at **54.3%**, though its share has declined significantly from 82.0% in the previous period as **3.8.13** has achieved massive adoption.
- **3.8.13** has emerged as a major release, capturing **38.1%** of users in just three weeks—an exceptionally rapid adoption rate.
- **3.8.11** has declined to **4.2%** (from 9.4%), likely as users upgraded to 3.8.13.
- **3.8.14** has appeared as a new version with **1.2%** adoption.


## 3. Minecraft Version Distribution

| Game Version | User Count | Share |
|--------------|------------|-------|
| **1.20.1** | **168,909** | **48.3%** |
| **1.21.1** | **122,569** | **35.1%** |
| 1.21.11 | 20,192 | 5.8% |
| 26.1.2 | 15,653 | 4.5% |
| 26.2 | 13,374 | 3.8% |
| 1.12.2 | 1,419 | 0.4% |
| 26.1 | 1,197 | 0.3% |
| 1.21.10 | 843 | 0.2% |
| 1.16.5 | 754 | 0.2% |
| 1.21.8 | 611 | 0.2% |
| (empty) | 466 | 0.1% |
| Others | 3,428 | 1.0% |

- **1.20.1 remains the leading game version** at **48.3%**, though its share has dropped from 68.9% in the previous period.
- **1.21.1** has grown substantially to **35.1%** (up from 20.1%), significantly narrowing the gap with 1.20.1.
- The “new scheme” versions (26.x) collectively account for **~8.9%**, up from ~5.6%, showing continued adoption of newer release trains.
- **1.21.11** holds steady at **5.8%** (up from 3.5%).


## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Forge** | **172,395** | **49.3%** |
| **Fabric** | **136,522** | **39.1%** |
| NeoForge | 40,444 | 11.6% |
| Quilt | 53 | <0.1% |
| Legacy-Fabric | 1 | <0.1% |

- **Forge remains the largest platform** at **49.3%**, though its share has declined significantly from 69.4% in the previous period.
- **Fabric** has grown to **39.1%** (up from 22.9%), gaining substantial ground.
- **NeoForge** has increased to **11.6%** (up from 7.7%), continuing its steady growth trajectory.


## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region | User Count | Share |
|----------------|------------|-------|
| **China Mainland** | **243,896** | **69.8%** |
| United States | 20,814 | 6.0% |
| Russia | 9,801 | 2.8% |
| France | 9,114 | 2.6% |
| Germany | 5,203 | 1.5% |
| United Kingdom | 3,040 | 0.9% |
| Japan | 2,919 | 0.8% |
| Brazil | 2,790 | 0.8% |
| Canada | 2,657 | 0.8% |
| Taiwan | 2,499 | 0.7% |

- **China Mainland remains the largest user base** at **69.8%**, roughly stable compared to the previous period (71.8%).
- The report covers users from **over 150 countries/regions**, demonstrating continued global reach.
- **France** maintains its position in the top 5 with a stable share of **2.6%**.


## 6. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform | Game Version | User Count | Description |
|----------|--------------|------------|-------------|
| **Forge** | **1.20.1** | **166,123** | **Overwhelmingly dominant combination** |
| Fabric | 1.21.1 | 85,648 | Fast-growing modern combination |
| NeoForge | 1.21.1 | 36,794 | Leading modern loader for latest versions |
| Fabric | 1.21.11 | 18,812 | Strong presence on latest release |
| Fabric | 26.1.2 | 12,978 | Early adopter combination for new scheme |

- The combination of **Forge + 1.20.1** remains the single largest configuration, representing **47.5%** of all user sessions.
- **Fabric** users are heavily concentrated on **1.21.1** (85,648 users), making it the second-largest platform-version pair.
- **NeoForge** has established a strong presence on **1.21.1** with 36,794 users.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.10** | **Forge** | **1.20.1** | **147,115** |
| 3.8.13 | Fabric | 1.21.1 | 60,254 |
| 3.8.10 | Fabric | 1.21.1 | 24,681 |
| 3.8.13 | NeoForge | 1.21.1 | 17,782 |
| 3.8.10 | NeoForge | 1.21.1 | 14,896 |
| 3.8.13 | Forge | 1.20.1 | 13,789 |

- **3.8.10 + Forge + 1.20.1** remains the single most popular configuration with nearly **147,000** users.
- **3.8.13** has achieved significant adoption across multiple platforms, with **Fabric + 1.21.1** leading at 60,254 users.
- The data shows a clear bifurcation: existing users staying on 3.8.10 + Forge + 1.20.1, while newer adopters gravitate toward 3.8.13 on Fabric/NeoForge + 1.21.1.


## 7. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.13 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://privacy.ellp.mods.hixland.com/privacy) for the latest terms.


## 8. Summary & Outlook

During this telemetry period (June 19 – July 10, 2026), Enchantment Level Language Patch has demonstrated significant ecosystem evolution:

- **Data Volume:** Total records reached **349,415** over 21 days. The decline in daily average compared to the previous period reflects natural user base decay over the extended window and the rapid version upgrade cycle (3.8.10 → 3.8.13) that may have reset session counters.

- **Version Revolution:** **3.8.13** has achieved an extraordinary **38.1%** adoption in just three weeks, marking one of the most successful version upgrades in the mod's history. **3.8.10** remains the largest single version (54.3%) but is steadily declining.

- **Game Version Shift:** **1.21.1** has grown to **35.1%** (up from 20.1%), significantly closing the gap with **1.20.1** (48.3%). The new scheme (26.x) now accounts for ~8.9% of users.

- **Platform Diversification:** **Forge** remains the largest platform (49.3%), but **Fabric** (39.1%) and **NeoForge** (11.6%) have both gained substantial share, reflecting a more balanced ecosystem.

- **Geographic Stability:** **China Mainland** remains the largest user base at ~70%, with global distribution remaining consistent.

- **Ecosystem Health:** The rapid adoption of **3.8.13** (38.1%) and the emergence of **3.8.14** (1.2%) demonstrate a vibrant, upgrade-oriented ecosystem with strong user engagement.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-07-10
