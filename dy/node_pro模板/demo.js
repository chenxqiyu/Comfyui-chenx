const args = process.argv.slice(2);

if (args.length === 0) {
    console.error('No parameters provided');
    process.exit(1);
}

try {
    // 解析传入的JSON参数
    const inputParams = JSON.parse(args[0]);
    
    // 处理业务逻辑
    const result = `Node.js processed: ${JSON.stringify(inputParams)}`;
    
    // 返回处理结果
    console.log(result);
} catch (err) {
    console.error(`Error: ${err.message}`);
    process.exit(1);
}