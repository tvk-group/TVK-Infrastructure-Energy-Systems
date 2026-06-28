#!/usr/bin/env node
import fs from "fs";
import path from "path";

function resolveMessageConflict(filePath) {
  let content = fs.readFileSync(filePath, "utf8");
  if (!content.includes("<<<<<<< HEAD")) {
    console.log(`No conflict: ${filePath}`);
    return;
  }

  const match = content.match(
    /<<<<<<< HEAD(?::[^\n]*)?\n([\s\S]*?)=======\n([\s\S]*?)>>>>>>> origin\/main(?::[^\n]*)?\n(\s*\}\n\})/
  );
  if (!match) {
    console.error(`Could not parse conflict in ${filePath}`);
    process.exit(1);
  }

  const appBlock = match[1].trim().replace(/,\s*$/, "");
  const seoBlock = match[2].trim().replace(/,\s*$/, "");
  const resolved = content.replace(match[0], `${appBlock},\n  ${seoBlock}\n}\n`);
  fs.writeFileSync(filePath, resolved);
  console.log(`Resolved: ${filePath}`);
}

for (const file of ["messages/en.json", "messages/tr.json", "messages/zh-cn.json"]) {
  resolveMessageConflict(path.join(process.cwd(), file));
}
