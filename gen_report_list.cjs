#!/usr/bin/env node

/**
 * gen_report_list.cjs
 * 用途：在 postinstall 时扫描 ./reports/ 目录，收集所有符合 $id 格式（三段式路径）且包含 en.md 和 zh.md 的子目录，
 *       将 $id 列表写入 ./reports.json。
 * 用法：node gen_report_list.cjs
 */

const fs = require('fs');
const path = require('path');

// 配置
const REPORTS_ROOT = path.join(process.cwd(), 'reports');   // ./reports
const OUTPUT_FILE = path.join(process.cwd(), 'reports.json'); // ./reports.json

// 验证 $id 是否由三部分组成（形如 a/b/c，允许任意字符，但必须非空且不含首尾斜杠）
const ID_SEGMENTS = 3;
function isValidId(id) {
    if (!id || typeof id !== 'string') return false;
    const parts = id.split('/');
    if (parts.length !== ID_SEGMENTS) return false;
    // 每个部分不能为空，且不能包含路径遍历等危险字符（简单检查）
    return parts.every(part => part.length > 0 && !part.includes('..') && !part.includes('\\'));
}

// 递归扫描 ./reports 下的所有目录，返回满足条件的 $id 数组
function collectReportIds(dir, currentRelativePath = '') {
    let results = [];

    // 读取目录内容
    let entries;
    try {
        entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch (err) {
        // 如果目录不存在或无法读取，静默忽略（例如 reports 目录尚未创建）
        if (err.code === 'ENOENT') {
            console.warn(`⚠️  Directory not found: ${dir}, skipping.`);
        } else {
            console.error(`❌ Failed to read directory ${dir}:`, err.message);
        }
        return results;
    }

    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        const nextRelative = currentRelativePath ? `${currentRelativePath}/${entry.name}` : entry.name;

        if (entry.isDirectory()) {
            // 先判断当前相对路径是否已经是三段式
            const parts = nextRelative.split('/');
            if (parts.length === ID_SEGMENTS) {
                // 已经是三级目录，检查该目录下是否存在 en.md 和 zh.md
                const enPath = path.join(fullPath, 'en.md');
                const zhPath = path.join(fullPath, 'zh.md');
                const hasEn = fs.existsSync(enPath);
                const hasZh = fs.existsSync(zhPath);
                if (hasEn && hasZh) {
                    // 验证 $id 格式合法性
                    if (isValidId(nextRelative)) {
                        results.push(nextRelative);
                    } else {
                        console.warn(`⚠️  Skipping invalid ID format: ${nextRelative}`);
                    }
                }
                // 注意：即使满足三级目录，也不继续向下递归（因为 $id 定义要求刚好三层）
                // 如果该目录下还有更深层目录，忽略
            } else if (parts.length < ID_SEGMENTS) {
                // 尚未达到三层，继续递归
                const deeper = collectReportIds(fullPath, nextRelative);
                results.push(...deeper);
            }
            // 如果 parts.length > 3，理论上不会出现，但可以忽略（不处理深层嵌套）
        }
        // 忽略文件
    }

    return results;
}

// 主流程
function main() {
    console.log('🔍 Scanning reports directories...');

    // 确保 reports 根目录存在
    if (!fs.existsSync(REPORTS_ROOT)) {
        console.warn(`⚠️  ${REPORTS_ROOT} does not exist. Creating empty reports.json.`);
        fs.writeFileSync(OUTPUT_FILE, JSON.stringify([], null, 2), 'utf8');
        console.log(`✅ Empty reports.json written (no reports found).`);
        return;
    }

    const idList = collectReportIds(REPORTS_ROOT);
    // 可选：对收集到的 id 进行排序（按字典序，通常日期越早越前，也可以自定义）
    idList.sort(); // 自然排序，例如 2026/04/05_a 会按字符串顺序

    // 写入 JSON 文件（格式化输出）
    try {
        fs.writeFileSync(OUTPUT_FILE, JSON.stringify(idList, null, 2), 'utf8');
        console.log(`✅ Generated ${OUTPUT_FILE} with ${idList.length} report(s).`);
        if (idList.length > 0) {
            console.log(`📋 First few IDs: ${idList.slice(0, 3).join(', ')}${idList.length > 3 ? '...' : ''}`);
        }
    } catch (err) {
        console.error(`❌ Failed to write ${OUTPUT_FILE}:`, err.message);
        process.exit(1);
    }
}

// 执行
main();