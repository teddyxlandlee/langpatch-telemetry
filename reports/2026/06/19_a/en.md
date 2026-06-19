# Telemetry Analysis Report (2026/06/12 – 2026/06/19)

**Posted by:** teddyxlandlee  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/be77774bbbf987941e3e08cd5bd84f3b)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **June 12, 2026 and June 19, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).


## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 213,562  
  During this 7-day period, a total of **213,562** valid telemetry records were reported.

  **Important Interpretation Note:** Compared to the previous period (293,100 records over 11 days, ~26,645/day), this period’s daily average (~30,509/day) shows a **modest increase of approximately 14.5%** . The apparent drop in total volume is primarily due to the shorter collection window, not a decline in user activity.

- **Schema version distribution:**
  - `schema_version 2`: **212,419** (99.5%)
  - `schema_version 1`: **1,143** (0.5%)

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).


## 2. Mod Version Distribution

| Version | User Count | Share |
|---------|------------|-------|
| **3.8.10** | **175,041** | **82.0%** |
| 3.8.11 | 19,988 | 9.4% |
| 3.8.6 | 7,300 | 3.4% |
| 3.8.4 | 5,194 | 2.4% |
| (empty) | 2,015 | 0.9% |
| 3.8.5 | 1,475 | 0.7% |
| 3.8.13 | 1,094 | 0.5% |
| 3.8.1 | 1,074 | 0.5% |
| 3.8.2 | 198 | 0.1% |
| 3.8.12 | 127 | 0.1% |
| 3.8.0 | 56 | <0.1% |

- **3.8.10 remains the dominant version**, accounting for **82.0%** of users, though its share has slightly declined from 84.9% in the previous period as newer versions gain traction.
- **3.8.11** continues to grow, now at **9.4%** (up from 6.8%).
- **3.8.13 and 3.8.12** have emerged as new versions, collectively capturing **0.6%** of users.
- Versions **3.8.5 and below** continue to decline, consistent with the server’s deprecation policy.


## 3. Minecraft Version Distribution

| Game Version | User Count | Share |
|--------------|------------|-------|
| **1.20.1** | **147,173** | **68.9%** |
| 1.21.1 | 42,824 | 20.1% |
| 26.1.2 | 10,579 | 5.0% |
| 1.21.11 | 7,580 | 3.5% |
| (empty) | 1,176 | 0.6% |
| 1.20.2 | 648 | 0.3% |
| 26.1 | 614 | 0.3% |
| 1.12.2 | 443 | 0.2% |
| Others | 2,525 | 1.2% |

- **1.20.1 remains the dominant game version** at **68.9%**, though its share has slightly decreased from 72.2% in the previous period.
- **1.21.1** has increased its share to **20.1%** (up from 18.4%), narrowing the gap with 1.20.1.
- The “new scheme” versions (26.x) collectively account for **~5.6%**, showing stable adoption among early adopters.


## 4. Mod Platform Distribution

| Platform | User Count | Share |
|----------|------------|-------|
| **Forge** | **148,162** | **69.4%** |
| Fabric | 48,963 | 22.9% |
| NeoForge | 16,407 | 7.7% |
| Quilt | 29 | <0.1% |
| Legacy-Fabric | 1 | <0.1% |

- **Forge remains the dominant platform** at **69.4%**, though its share has slightly declined from 73.0% in the previous period.
- **Fabric** has increased its share to **22.9%** (up from 19.4%), recovering some ground.
- **NeoForge** holds steady at **7.7%** (up slightly from 7.6%).


## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region | User Count | Share |
|----------------|------------|-------|
| **China Mainland** | **153,411** | **71.8%** |
| United States | 12,574 | 5.9% |
| Russia | 5,767 | 2.7% |
| France | 5,488 | 2.6% |
| Germany | 3,216 | 1.5% |
| United Kingdom | 1,806 | 0.8% |
| Brazil | 1,773 | 0.8% |
| Japan | 1,755 | 0.8% |
| Taiwan | 1,715 | 0.8% |
| Canada | 1,591 | 0.7% |

- **China Mainland remains the largest user base** at **71.8%**, though its share has slightly decreased from 76.5% in the previous period.
- **France** has entered the top 10 with **5,488 users (2.6%)**, a notable presence.
- The report covers users from **over 150 countries/regions**, demonstrating continued global reach.


## 6. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform | Game Version | User Count | Description |
|----------|--------------|------------|-------------|
| **Forge** | **1.20.1** | **146,113** | **Overwhelmingly dominant combination** |
| Fabric | 1.21.1 | 27,585 | Secondary combination, still significant |
| NeoForge | 1.21.1 | 15,157 | Stable modern loader for latest versions |
| Fabric | 26.1.2 | 9,875 | Early adopter combination for new scheme |
| Fabric | 1.21.11 | 7,314 | Previous latest release |

- The combination of **Forge + 1.20.1** remains the absolute standard, representing **68.4%** of all user sessions.
- **Fabric** users are more distributed across newer game versions (1.21.1, 26.1.2, 1.21.11), while Forge users remain heavily concentrated on 1.20.1.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.10** | **Forge** | **1.20.1** | **139,749** |
| 3.8.10 | Fabric | 1.21.1 | 26,361 |
| 3.8.10 | NeoForge | 1.21.1 | 6,062 |
| 3.8.4 | Fabric | 26.1.2 | 4,722 |
| 3.8.11 | NeoForge | 1.21.1 | 4,523 |
| 3.8.11 | Fabric | 1.21.11 | 4,284 |

- **3.8.10 + Forge + 1.20.1** remains the single most popular configuration by a massive margin, with nearly **140,000** users.
- **3.8.11** is gaining traction across multiple platforms and game versions, indicating healthy version adoption.


## 7. Server Status

The telemetry backend on Tencent Cloud (Hong Kong SAR) continues to operate normally. As previously announced, the server **no longer accepts telemetry from versions 3.8.5 and below**. Users are encouraged to use **v3.8.10 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://telemetry.langpatch.mc.7c7.icu/privacy) for the latest terms.


## 8. Summary & Outlook

During this telemetry period (June 12–19, 2026), Enchantment Level Language Patch has demonstrated continued stability and healthy ecosystem evolution:

- **Data Volume & Coverage:** Daily average telemetry records increased by approximately **14.5%** compared to the previous period, suggesting stable or growing active user engagement.

- **Version Consolidation:** Mod version **3.8.10** (82.0%) and game version **1.20.1** (68.9%) remain the absolute standards, though both are gradually ceding share to newer versions (3.8.11, 1.21.1).

- **Platform Landscape:** **Forge** remains the dominant platform (69.4%), with **Fabric** recovering some ground (22.9%) and **NeoForge** holding steady (7.7%).

- **Geographic Distribution:** **China Mainland** remains the largest user base (71.8%), with a slight decrease from the previous period suggesting a more balanced global distribution.

- **Ecosystem Maturity:** The successful adoption of **3.8.11** (9.4%) and the emergence of **3.8.13** demonstrate a healthy, upgrade-oriented ecosystem.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-06-19