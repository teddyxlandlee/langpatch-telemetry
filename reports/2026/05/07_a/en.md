### EnchLevel-LangPatch Monthly Telemetry Snapshot (April 2026 Review)

**Release Date:** May 7, 2026  
**Reporting Period:** April 5, 2026 – May 6, 2026  
**Total Samples:** 84,526 transmissions

Hello, I am the developer of EnchLevel-LangPatch. In line with our commitment to transparency, I have compiled the anonymous telemetry data from last month. This report contains **no personal identification information** (IP/UUID) and is solely used to analyze the mod's operating environment and ecosystem distribution.

#### 1. Telemetry Participation & Data Quality
First, regarding the source of the data:
- **Privacy Preferences:** The data shows that all samples are `telemetry_level: lvl1`. This means **no users have actively enabled "Detailed Mode"**. This aligns with expectations, as most users tend to stick with default settings or disable telemetry entirely for privacy.
- **Version Consistency:** In the `mod_version` dimension, the vast majority of users are concentrated on the latest version (3.8.5), indicating that players generally keep the mod up to date.
- **Schema Distribution:** The ratio of data structure versions (Schema) is approximately **13:71**, further corroborating that the majority of users are running clients compatible with the latest specifications.

#### 2. Core Environment Analysis (Platform & Minecraft)
This is the highlight of the analysis. Let's look at the distribution of `platform_mcv` (Platform + Game Version).

**Mainstream Ecosystem (Occupying over 80% of the share):**
- **Fabric + 1.21.11:** This is currently the largest user group. Fabric remains the preferred choice for high-version modding, and users are upgrading very rapidly.
- **NeoForge + 1.21.1:** As NeoForge matures, it has garnered a significant following on the stable 1.21.1 version.
- **Forge + 1.20.1:** The "rock-solid" veteran. In the 1.20.x era, Forge still maintains a powerful presence with an extremely stable user base.

**Bleeding Edge & Niche Environments (Small numbers, but fascinating):**
Telemetry also captured some unconventional environments, proving the mod's wide compatibility coverage:
- **Minecraft 26.x Series:** A notable highlight. Data shows a significant number of users (approx. 7,454) have upgraded to the **26.1.2** release, and some geeks are even testing the **26.2-snapshot** builds. This indicates a strong willingness among core players to experiment with new technology.
- **Legacy Versions:** Users are still active on `1.12.2` and `1.16.5`. Although EnchLevel-LangPatch focuses on newer versions, compatibility with these legacy environments is a pleasant surprise.
- **Niche Platforms:** Quilt, while a tiny fraction (only 229 transmissions), is present, proving the effectiveness of cross-platform compatibility layers.

#### 3. Feature Usage: LangPatch API
Data regarding extended functionality is thought-provoking:
- **Hooks Data is Empty:** In the `current_hooks` and `all_hooks` dimensions, data for `enchantment` and `potion` is empty (`{}`).
- **Conclusion:** This indicates that the LangPatch Java API and third-party extension mechanisms are **not widely used**.
- **Developer Self-Reflection:** I personally believe this is largely because I haven't done a good job promoting the API and documentation. Currently, most users treat EnchLevel-LangPatch as an "out-of-the-box" translation mod, rather than digging its potential as a "translation development library." This is an area for future improvement.

#### 4. Geographic & Time Distribution
- **Primary Distribution:** The data shows distinct regional characteristics.
    - **China (China / Shanghai):** Undoubtedly the core region, holding the largest share. This aligns with my (the developer's) community environment.
    - **North America & Europe:** Users in the United States, Germany, the UK, and Russia form the second tier, with a relatively even distribution.
- **Diversity:** While the core is in East Asia and North America, the data also includes transmissions from Southeast Asia (Thailand, Vietnam), South America (Brazil), and the Middle East, reflecting the global diversity of the Minecraft community.

#### 5. Issues to Investigate
- **Empty MC Version:** There are `3,203` records with an empty string (`""`) for `mc_version`.
- **Status:** The cause is currently unknown. This could be due to specific launcher environments, conflicts with very old mod loaders, or rare runtime exceptions causing capture failures. More detailed diagnostic logic needs to be added in future versions to pinpoint this.

---

#### Raw Data (JSON)
For the sake of total transparency, the unprocessed raw aggregated data is uploaded to [GitHub Gist](https://gist.github.com/teddyxlandlee/ac3804fe501cfae20aefbd7e36c4ec29).

*Report drafted by Qwen AI*