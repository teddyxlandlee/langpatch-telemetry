# 🛡️ Privacy Policy | 隐私政策

> **🌏 Language / 语言选择**
> - [English Version](#english-version)
> - [中文版](#中文版)

---

## English Version

**Last Updated:** June 3, 2026

This mod (EnchLevel-LangPatch) respects your privacy. We collect telemetry data only with your explicit consent to help us improve the stability and functionality of the software. You have full control over the level of data collection at any time via the configuration file.

### 1. What Data We Collect

Depending on your settings in `config/enchlevel-langpatch-telemetry.txt`, we may collect the following information:

- **Necessary (Level 0)**
  - **Schema Version:** To identify the data structure version.
  - **Client Time:** For timestamp synchronization.
  - **Request Timeout & Relay Status:** Request timeout occurrences and whether the telemetry data was relayed via Netlify (for legacy clients).
  - *This level does not collect any personal information or specific in-game data.*

- **Functional (Level 1)**
  - In addition to the necessary data, we collect:
  - **Game Environment:** Minecraft version, mod loader (e.g., Fabric/Forge), and mod version.
  - **Geolocation:** Country code and time zone (used to analyze regional usage patterns).
  - **Current Hook State:** Resource locations of currently active enchantments and potion effects.

- **Optional (Level 2)**
  - In addition to functional data, we collect:
  - **Full Registry List:** A complete list of all enchantment and potion effect resource locations registered in your environment. This helps us understand potential features that are not being utilized.

### 2. How We Use This Data

The collected data is used solely for the following purposes:

- **Troubleshooting:** Identifying and fixing software bugs.
- **Feature Optimization:** Prioritizing development based on usage frequency.
- **Compatibility Analysis:** Ensuring the mod remains compatible with different versions of Minecraft and other mods.

### 3. Data Storage and Security

- **Anonymity:** We do not collect your username, UUID, or IP address. All data is transmitted anonymously.
- **Secure Transmission:** Data is signed during transmission to ensure integrity.
- **Geolocked Storage:** All collected data is securely stored in **Tencent Cloud Object Storage (COS)**.
  - **Region:** The backend code explicitly specifies the region as **`ap-hongkong` (Hong Kong, China)**. This ensures your data remains within the defined geographical boundary.
  - **Legacy Relay:** Some data from older mod versions may have been relayed via Netlify Edge Functions. Newer versions directly use Tencent SCF + COS.
- **Retention:** We do not currently employ an automated deletion schedule. Data is retained only as long as necessary for analysis purposes. Old data may be overwritten or manually purged periodically based on storage capacity and analysis needs.

### 4. Your Control

You have full control. You can adjust the telemetry level at any time by creating/modifying the `config/enchlevel-langpatch-telemetry.txt` file:

- **Disabled (-1):** Completely stops data transmission.
- **Necessary (0):** Sends only basic operational data.
- **Functional (1):** Helps us improve functionality (Default).
- **Optional (2):** Sends all data to support in-depth development.

### 5. Infrastructure and Open Source Transparency

To ensure transparency and security, our telemetry backend architecture is fully open source:

- **Source Code:** Our backend logic (including Tencent SCF functions) is open-sourced under the **AGPL-3.0** license. You can review the code at any time on GitHub:
  - Repository: [teddyxlandlee/langpatch-telemetry-v2](https://github.com/teddyxlandlee/langpatch-telemetry-v2)
- **Current Data Flow:** Your data is sent directly to **Tencent SCF (Serverless Cloud Function)**, which then writes it to **Tencent COS**.
- **Legacy Relay (Old Versions):** Older mod versions used Netlify Edge Functions as a relay due to technical constraints. Those relays operated under a strict **no-log policy** — they did not store, log, or analyze any data; data was discarded immediately after forwarding.

### 6. Contact Us

If you have any questions, concerns, or requests regarding this Privacy Policy or our data processing practices, please contact us via the following methods:

- **Mod Issues**: [teddyxlandlee/enchlevel-langpatch](https://github.com/teddyxlandlee/enchlevel-langpatch/issues)
- **Email**: [teddyxlandlee@hotmail.com](mailto:teddyxlandlee@hotmail.com)

We aim to respond to all legitimate requests within 30 days.

---

## 中文版

**最后更新日期：** 2026年6月3日

本模组（EnchLevel-LangPatch）尊重您的隐私。我们仅在您明确同意的情况下收集遥测数据，旨在帮助我们改进软件的稳定性与功能。您可以随时通过配置文件完全控制数据的收集级别。

### 1. 我们收集哪些数据？

根据您在 `config/enchlevel-langpatch-telemetry.txt` 中的设置，我们可能会收集以下信息：

- **必要数据 (Necessary / Level 0)**
  - **Schema 版本**：用于识别数据结构的版本号。
  - **客户端时间**：用于同步时间戳。
  - **请求超时与中继状态**：请求超时发生情况，以及遥测数据是否经过 Netlify 中转（仅限旧版客户端）。
  - *此级别不收集任何个人身份信息或游戏内具体数据。*

- **功能改进数据 (Functional / Level 1)**
  - 除了上述必要数据外，我们还会收集：
  - **游戏环境信息**：Minecraft 版本号、模组加载器（如 Fabric/Forge）及模组版本。
  - **地理信息**：国家代码和时区（用于分析区域性的使用习惯）。
  - **当前钩子状态**：当前生效的附魔和药水效果的资源位置（Resource Location）。

- **可选数据 (Optional / Level 2)**
  - 除了功能改进数据外，我们还会收集：
  - **完整列表**：您当前环境中注册的所有附魔和药水效果的完整列表（Resource Locations）。这有助于我们了解未被使用的潜在功能。

### 2. 我们如何使用这些数据？

收集到的数据仅用于以下目的：

- **故障排查**：识别和修复软件错误。
- **功能优化**：根据使用频率调整开发优先级。
- **兼容性分析**：确保模组与不同版本的 Minecraft 和其他模组保持兼容。

### 3. 数据存储与安全性

- **匿名性**：我们不收集您的用户名、UUID 或 IP 地址。所有数据均为匿名传输。
- **加密传输**：数据在传输过程中使用签名机制确保完整性。
- **地域锁定存储**：所有收集到的数据将安全地存储在 **腾讯云对象存储（Tencent COS）** 服务中。
  - **区域**：后端代码中已硬编码指定了区域为 **`ap-hongkong`（中国香港）**。这确保了您的数据物理上仅存储于该地理边界内。
  - **旧版中继**：部分来自旧版模组的数据可能曾经过 Netlify Edge Functions 中转。新版本直接使用腾讯云 SCF + COS。
- **存储期限**：目前我们未设置自动删除计划。数据仅在分析所需的期限内保留。根据存储容量和分析需求，旧数据可能会被覆盖或进行不定期的手动清理。

### 4. 你的控制权

你拥有完全的控制权。你可以随时创建/修改 `config/enchlevel-langpatch-telemetry.txt` 文件来调整数据收集级别：

- **Disabled (-1)**：完全停止数据发送。
- **Necessary (0)**：仅发送基本运行数据。
- **Functional (1)**：帮助我们改进功能（默认设置）。
- **Optional (2)**：发送所有数据以支持深度开发。

### 5. 基础设施与开源声明

为了确保数据传输的安全性与透明度，我们的遥测后端架构完全开源：

- **开源代码库**：我们的后端处理逻辑（包括腾讯云 SCF 函数）均采用 **AGPL-3.0** 协议开源。您可以随时在 GitHub 上审查代码：
  - 仓库地址：[https://github.com/teddyxlandlee/langpatch-telemetry-v2](https://github.com/teddyxlandlee/langpatch-telemetry-v2)
- **当前数据流**：您的数据直接发送至 **腾讯云 SCF（无服务器云函数）**，再由其写入 **腾讯云 COS**。
- **旧版中继（旧版本）**：旧版模组曾因技术限制使用 Netlify Edge Functions 进行中转。这些中继服务器遵循严格的 **不落地原则** —— 不存储、不记录、不分析任何数据，处理完成后立即丢弃。

### 6. 联系我们

如果您对本隐私政策或我们的数据处理实践有任何疑问、意见或请求，请通过以下方式联系我们：

- **模组 Issues**：[teddyxlandlee/enchlevel-langpatch](https://github.com/teddyxlandlee/enchlevel-langpatch/issues)
- **电子邮箱**：[teddyxlandlee@hotmail.com](mailto:teddyxlandlee@hotmail.com)

我们力争在 30 天内回复所有合法的请求。