# Telemetry Analysis Report (2026/06/02 – 2026/06/12)

**Posted by:** teddyxlandlee  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/437c30716b6a2ff88459fcbb3ab51edd)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **June 2, 2026 and June 12, 2026**.

> **Privacy & Transparency Commitment**: This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)).

---

## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 293,100  
  During this 11-day period, a total of **293,100** valid telemetry records were reported.

  **Important Interpretation Note:** We hold the opinion that this significant increase in data volume is **primarily due to the resolution of prior data loss issues during the server migration, rather than a surge in active users**. The previous telemetry endpoint (Netlify Functions) suffered from packet loss and timeout issues, especially for users in China, causing many reports to be dropped. The migration to Tencent Cloud (Hong Kong SAR) largely resolved these connectivity problems, allowing previously lost telemetry to be successfully delivered. The “tripling” reflects improved data capture, not a tripling of the user base.

- **Schema version distribution:**
    - `schema_version 2`: **291,242** (99.4%)
    - `schema_version 1`: **1,858** (0.6%)

- **Telemetry Level:** All records are at `"lvl1"` (Functional level).

---

## 2. Mod Version Distribution

| Version | User Count | Share     | Change vs. Prev. Period |
|---------|------------|-----------|--------------------------|
| **3.8.10** | **248,987** | **84.9%** | ↑ **79.3%** |
| 3.8.11  | 19,799     | 6.8%      | New                      |
| 3.8.6   | 11,586     | 4.0%      | ↓ **60.1%**              |
| 3.8.4   | 5,350      | 1.8%      | ↓ 4.6%                   |
| (empty) | 2,852      | 1.0%      | ↓ 2.3%                   |
| 3.8.5   | 2,448      | 0.8%      | ↓ **13.4%**              |
| 3.8.1   | 1,717      | 0.6%      | ↓ 4.4%                   |
| 3.8.2   | 242        | 0.1%      | ↓ 0.9%                   |
| 3.8.0   | 119        | <0.1%     | ↓ 0.5%                   |

- **3.8.10 has become the overwhelmingly dominant version**, accounting for **84.9%** of users, a massive jump from 5.6% in the previous period.
- **3.8.11**, a new version, has already captured **6.8%** of users.
- Versions **3.8.6 and below have seen a sharp decline**, likely due to the server migration which stopped accepting data from versions older than 3.8.6. This confirms the effectiveness of the upgrade incentive.

---

## 3. Minecraft Version Distribution

| Game Version | User Count | Share     | Change vs. Prev. Period |
|--------------|------------|-----------|--------------------------|
| **1.20.1**     | **211,661** | **72.2%** | ↑ **50.2%**              |
| 1.21.1       | 53,845     | 18.4%     | ↓ 13.8%                  |
| 26.1.2       | 10,902     | 3.7%      | ↓ 9.6%                   |
| 1.21.11      | 9,494      | 3.2%      | ↓ **16.1%**              |
| (empty)      | 1,674      | 0.6%      | -                        |
| 1.12.2       | 912        | 0.3%      | ↓ 1.3%                   |
| Others       | 4,612      | 1.6%      | ↓ 6.5%                   |

- **1.20.1 has surged to become the dominant game version**, now accounting for **72.2%** of users. This is a significant shift from the previous period where it held 22.0%.
- **1.21.1** remains in second place but its share has decreased to **18.4%**.
- The "new scheme" versions (26.x) have seen a reduction in share, as the user base has consolidated heavily around 1.20.1.
- The data suggests a strong correlation between the rise of mod version 3.8.10 and game version 1.20.1.

---

## 4. Mod Platform Distribution

| Platform     | User Count | Share     | Change vs. Prev. Period |
|--------------|------------|-----------|--------------------------|
| **Forge**      | **213,877** | **73.0%** | ↑ **47.7%**              |
| Fabric       | 56,936     | 19.4%     | ↓ **22.9%**              |
| NeoForge     | 22,280     | 7.6%      | ↓ **24.8%**              |
| Quilt        | 7          | <0.1%     | -                        |

- **Forge has overtaken Fabric as the most popular platform** by a large margin, now holding **73.0%** of users.
- Both **Fabric** and **NeoForge** have seen significant drops in relative share, although their absolute user counts may have remained stable or grown slightly.
- This inversion of platform preference is directly tied to the massive increase in users on the **Forge + 1.20.1** combination.

---

## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region          | User Count | Share     | Change vs. Prev. Period |
|-------------------------|------------|-----------|--------------------------|
| 🇨🇳 **China**            | **224,360** | **76.5%** | ↑ **37.2%**              |
| 🇺🇸 United States        | 15,489     | 5.3%      | ↓ 6.4%                   |
| 🇷🇺 Russia               | 6,566      | 2.2%      | ↓ 3.8%                   |
| 🇩🇪 Germany              | 3,600      | 1.2%      | ↓ 3.6%                   |
| 🇬🇧 United Kingdom       | 2,597      | 0.9%      | ↓ 1.5%                   |
| 🇧🇷 Brazil               | 2,275      | 0.8%      | ↓ 1.6%                   |
| 🇨🇦 Canada               | 2,242      | 0.8%      | ↓ 0.8%                   |
| 🇯🇵 Japan                | 2,169      | 0.7%      | -                        |
| 🇭🇰 Hong Kong (SAR)      | 2,048      | 0.7%      | -                        |
| 🇻🇳 Vietnam              | 1,987      | 0.7%      | ↓ 1.0%                   |

- **China's user base has expanded dramatically**, now representing over **three-quarters (76.5%)** of all telemetry data.
- The geographic distribution has become more concentrated, with the top 3 countries now accounting for 84% of users (up from 57% previously).
- The report covers users from **163 other countries/regions**, demonstrating continued global reach, though with a stronger center of gravity in Asia.

### ⏰ Top 5 Timezones

| Timezone               | User Count | Corresponding Regions                     |
|------------------------|------------|-------------------------------------------|
| **Asia/Shanghai**      | **216,301** | Mainland China (73.8%)                    |
| America/New_York       | 5,043      | Eastern US, Eastern Canada                |
| America/Chicago        | 3,830      | Central US                                |
| Europe/Moscow          | 2,841      | Western Russia                            |
| Europe/Berlin          | 2,622      | Germany, Central Europe                   |

- Timezone data strongly corroborates the geographic findings, with **UTC+8 (Asia/Shanghai)** now representing nearly **74%** of the user base.

---

## 6. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform     | Game Version | User Count | Description                                        |
|--------------|--------------|------------|----------------------------------------------------|
| **Forge**    | **1.20.1**   | **210,582** | **Overwhelmingly dominant combination**          |
| Fabric       | 1.21.1       | 33,226     | Secondary combination, still significant          |
| NeoForge     | 1.21.1       | 20,498     | Stable modern loader for latest versions          |
| Fabric       | 26.1.2       | 10,107     | Early adopter combination for new scheme          |
| Fabric       | 1.21.11      | 9,125      | Previous latest release                           |

- The combination of **Forge + 1.20.1** has become the absolute standard, representing **71.8%** of all user sessions.
- **Fabric** users are more distributed across newer game versions (1.21.1, 26.1.2, 1.21.11), while Forge users are heavily concentrated on 1.20.1.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| **3.8.10**  | **Forge**  | **1.20.1**   | **203,166** |
| 3.8.10      | Fabric   | 1.21.1       | 31,955      |
| 3.8.10      | NeoForge | 1.21.1       | 7,563       |
| 3.8.6       | NeoForge | 1.21.1       | 5,504       |
| 3.8.11      | NeoForge | 1.21.1       | 4,101       |

- **3.8.10 + Forge + 1.20.1** is the single most popular configuration by a massive margin, with over 200,000 users.
- This combination did not even appear in the top 5 of the previous report, highlighting a major ecosystem shift.

---

## 7. Server Migration Notice – Update

The server migration to Tencent Cloud (Hong Kong SAR) is complete. As previously announced, the new server **no longer accepts telemetry from versions 3.8.5 and below**. Please ensure you are using **v3.8.10 or higher** to continue contributing.

> Please refer to the [Privacy Policy page](https://telemetry.langpatch.mc.7c7.icu/privacy) for the latest terms.

---

## 8. Summary & Outlook

During this short telemetry period (June 2–12, 2026), Enchantment Level Language Patch has demonstrated a successful infrastructure migration and improved data quality:

- **Data Volume & Coverage:** Telemetry records tripled after the migration. However, this increase primarily reflects the resolution of previous data loss issues on Netlify Functions, rather than a tripling of the active user base. The “surge” indicates that the new server is successfully capturing telemetry that was previously dropped due to packet loss and timeouts, especially for users in China.

- **Version Consolidation:** Mod version **3.8.10** (84.9%) and game version **1.20.1** (72.2%) are now the absolute standards, a drastic change from the previous period.

- **Platform Realignment:** **Forge** has become the dominant platform (73.0%), overtaking Fabric. This is directly linked to the massive popularity of the Forge + 1.20.1 combination.

- **Geographic Concentration:** The mod's user base has become heavily centered in **China (76.5%)**, up from 39.3% in the last report. This is likely due to the new server's better connectivity to Chinese users, not an actual demographic shift.

- **Ecosystem Maturity:** The successful deprecation of older mod versions (3.8.5 and below) shows a healthy, upgrade-oriented ecosystem. This deprecation is also a result of technical enforcement by the new server, which stopped accepting data from these legacy versions.

> **Data Interpretation Note:** The apparent tripling of “user count” is largely attributable to the elimination of prior data loss, not a threefold increase in the actual user population. Please interpret user growth metrics with caution when comparing pre- and post-migration data.

Thank you for your continued support and for keeping your mod updated!

**Posted by:** teddyxlandlee  
**Date:** 2026-06-12