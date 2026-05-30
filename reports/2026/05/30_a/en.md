# Telemetry Analysis Report (2026/05/07–2026/05/30) – Revised

**Posted by:** teddyxlandlee  
**Raw Data:** [GitHub Gist](https://gist.github.com/teddyxlandlee/e9f769dbe03d6405e3127581f90fed94)

This report is based on anonymous telemetry data collected by Enchantment Level Language Patch between **7 May 2026 and 30 May 2026**. The data covers mod version distribution, Minecraft version distribution, mod platform distribution, and player geolocation, helping you understand the ecosystem and user behavior trends of the mod.

> **Privacy & Transparency Commitment**: In keeping with our privacy policy transparency commitment, I have compiled the anonymous telemetry data from the past month. This report contains no personally identifiable information (IP/UUID) and is used solely to analyze the mod's runtime environment and ecosystem distribution.

> 📌 **Data Note**: This report only includes data from users who have explicitly consented to telemetry collection (telemetry level ≥ Functional (Level 1)). If you prefer not to participate in telemetry, you can set the telemetry level to `-1` in the configuration file to completely disable data transmission.

---

## 1. Telemetry Participation & Data Quality

### Overview
- **Total telemetry records:** 98,122  
  During this period, a total of **98,122** valid telemetry records were reported, each representing one game session (typically a client launch instance).

- **Schema version distribution:**
    - `schema_version 2`: **92,644** (94.5%)  
      The vast majority of telemetry data has been upgraded to a newer data structure, simplifying data parsing.
    - `schema_version 1`: **5,478** (5.5%)  
      A small residual of older data, expected to gradually disappear as older user bases naturally decline.

- **Telemetry Level:** Among all 98,122 records, the telemetry level is `"lvl1"` (Functional level), meaning functional data is sent, but **not** the optional full registry list (Level 2). This indicates that the majority of users who participate in telemetry have retained the default telemetry settings.

---

## 2. Mod Version Distribution

| Version | User Count | Share     |
|---------|------------|-----------|
| 3.8.6   | 62,821     | 64.1%     |
| 3.8.5   | 13,900     | 14.2%     |
| 3.8.4   | 6,319      | 6.4%      |
| 3.8.10  | 5,457      | 5.6%      |
| 3.8.1   | 4,923      | 5.0%      |
| 3.8.2   | 946        | 1.0%      |
| 3.8.0   | 500        | 0.5%      |
| Not reported | 3,256 | 3.3%      |

- The latest stable version **3.8.6** dominates, accounting for **64.1%** of users.
- **3.8.10**, while only representing **5.6%**, is already showing growth potential.
- Versions **3.8.5 and above** together account for over **84%**, indicating low version fragmentation and a relatively concentrated ecosystem.

> 💡 **Server Migration Notice**: **After the migration is complete, the telemetry server will no longer be able to receive data from v3.8.5 and below**. Data from versions lower than 3.8.6 will no longer be included in analysis reports. It is recommended that users upgrade to 3.8.6+ at their convenience to continue supporting telemetry analysis.

---

## 3. Minecraft Version Distribution

| Game Version   | User Count | Share     |
|----------------|------------|-----------|
| 1.21.1         | 31,561     | 32.2%     |
| 1.20.1         | 21,540     | 22.0%     |
| 1.21.11        | 18,934     | 19.3%     |
| 26.1.2         | 13,048     | 13.3%     |
| 26.1           | 1,603      | 1.6%      |
| 1.12.2         | 1,525      | 1.6%      |
| 1.21.10        | 1,043      | 1.1%      |
| 26.1.1         | 891        | 0.9%      |
| Others         | 7,977      | 8.1%      |

- **1.21.1** and **1.20.1** are still the two most popular versions, together accounting for over **54%**.
- **1.21.11** (the previous latest official release) accounts for **19.3%**, while the newer **26.1.2** has reached **13.3%**, indicating rapid adoption of new game versions.
- **26.1** and **26.1.1** together account for **2.5%**, showing a smooth transition.
- Classic versions like **1.12.2** still have a stable user base.

---

## 4. Mod Platform Distribution

| Platform     | User Count | Share   |
|--------------|------------|---------|
| Fabric       | 41,465     | 42.3%   |
| NeoForge     | 31,773     | 32.4%   |
| Forge        | 24,861     | 25.3%   |
| Quilt        | 18         | <0.1%   |
| Legacy Fabric| 5          | <0.1%   |

- **Fabric** remains the most popular mod platform, accounting for **42.3%**.
- **NeoForge** (32.4%) and **Forge** (25.3%) together account for **57.7%** of users, demonstrating the diversity of the mod loader ecosystem.
- **Quilt** and **Legacy Fabric** have only a minimal share.

---

## 5. Geographic Distribution

### 🌏 Top 10 Countries/Regions

| Country/Region          | User Count | Share     |
|-------------------------|------------|-----------|
| 🇨🇳 China                | 38,544     | 39.3%     |
| 🇺🇸 United States        | 11,483     | 11.7%     |
| 🇷🇺 Russia               | 5,901      | 6.0%      |
| 🇩🇪 Germany              | 4,741      | 4.8%      |
| 🇬🇧 United Kingdom       | 2,364      | 2.4%      |
| 🇧🇷 Brazil               | 2,360      | 2.4%      |
| 🇵🇱 Poland               | 1,883      | 1.9%      |
| 🇻🇳 Vietnam              | 1,679      | 1.7%      |
| 🇰🇷 South Korea          | 1,666      | 1.7%      |
| 🇨🇦 Canada               | 1,577      | 1.6%      |

> Users from another **163** countries/regions also use the mod, totaling **25,924** users, demonstrating the mod's global reach.

- **China** accounts for nearly **40%** of users.
- **United States** (11.7%), **Russia** (6.0%), **Germany** (4.8%) follow.
- Global coverage spans Asia, Europe, Americas, and Oceania.

### ⏰ Top 10 Timezones

| Timezone               | User Count | Corresponding Regions                     |
|------------------------|------------|-------------------------------------------|
| Asia/Shanghai          | 38,451     | Mainland China                            |
| America/New_York       | 4,774      | Eastern US, Eastern Canada                |
| Europe/Berlin          | 4,741      | Germany, most of Central Europe           |
| Europe/Moscow          | 3,587      | Western Russia                            |
| America/Chicago        | 3,310      | Central US                                |
| Europe/London          | 2,364      | United Kingdom                            |
| Asia/Bangkok           | 2,115      | Thailand, Vietnam, Indochina              |
| America/Los_Angeles    | 2,102      | Western US, Western Canada                |
| Europe/Warsaw          | 1,883      | Poland                                    |
| Asia/Seoul             | 1,666      | South Korea                               |

- Timezone distribution closely matches geographic distribution.
- **UTC+8 (Asia/Shanghai)** has the highest concentration at **39.2%**.
- Coverage spans all 24 time zones.

---

## 6. Combined Analysis

### Most Popular Combinations (Platform + Game Version)

| Platform     | Game Version | User Count | Description                               |
|--------------|--------------|------------|-------------------------------------------|
| NeoForge     | 1.21.1       | 28,221     | Classic version + modern loader           |
| Forge        | 1.20.1       | 18,821     | Stable classic version + traditional loader |
| Fabric       | 1.21.11      | 17,997     | Previous latest release + lightweight platform |
| Fabric       | 26.1.2       | 11,471     | Current latest release + fast-iteration platform |
| Fabric       | 1.21.1       | 3,253      | Early latest version + lightweight platform |

- **NeoForge + 1.21.1** remains the most popular combination.
- **Fabric + 26.1.2** has grown to 11,471 users, showing Fabric's agility in adopting new version schemes.
- **Forge + 1.20.1** remains stable.

### Most Popular Combinations (Mod Version + Platform + Game Version)

| Mod Version | Platform | Game Version | User Count |
|-------------|----------|--------------|------------|
| 3.8.6       | NeoForge | 1.21.1       | 17,371     |
| 3.8.6       | Forge    | 1.20.1       | 14,126     |
| 3.8.6       | Fabric   | 1.21.11      | 11,741     |
| 3.8.6       | Fabric   | 26.1.2       | 7,664      |
| 3.8.1       | NeoForge | 1.21.1       | 4,424      |

- **3.8.6** is the dominant mod version across all major combinations.
- **3.8.6 + Fabric + 26.1.2** is now the fourth largest combination, reflecting fast adoption of the latest release.

---

## 7. Server Migration Notice

Important architectural changes are coming to the telemetry backend:

- **Data Storage Location Change**: Moving from Alibaba Cloud OSS (Shanghai node) to **Tencent Cloud (Hong Kong SAR, China)**.
- **Service Provider Change**: Switching from Alibaba Cloud to **Tencent Cloud**.
- **Privacy Policy Update**: The *Privacy Policy* will be revised accordingly to comply with new requirements.
- **Compatibility Change**: After migration, the server will **no longer accept telemetry data from v3.8.5 and below**. If you are using 3.8.5 or lower, please upgrade to **v3.8.6 or higher** to ensure continued telemetry recording.

> The privacy policy will be updated before migration. Please see the [Privacy Policy page](https://telemetry.langpatch.mc.7c7.icu/privacy) for the latest terms.

---

## 8. Summary & Outlook

During this telemetry period (May 7–30, 2026), Enchantment Level Language Patch demonstrated a stable user ecosystem:

- **User Scale**: Over **98,000** valid records, covering **160+** countries/regions.
- **Version Update**: **3.8.6** has become the absolute mainstream version (>64%).
- **Game Versions**: **1.21.1** (32.2%) and **1.20.1** (22.0%) are still major, but the new-scheme version **26.1.2** has rapidly reached **13.3%**, indicating a healthy migration to Mojang's new versioning.
- **Mod Platforms**: Balanced ecosystem across Fabric (42.3%), NeoForge (32.4%), and Forge (25.3%).
- **Geographic Distribution**: China accounts for nearly 40% of users, 3.5 times that of the US, reflecting the mod's strong influence in the Chinese community.

With the upcoming server migration and continued iteration, the telemetry system will more stably and compliantly support mod optimization. Thank you again for your support and trust!

**Posted by:** teddyxlandlee  
**Date:** 2026-05-30 (Revised)