using System;
using System.Text.Json;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("No parameters provided");
            return;
        }

        try
        {
            // 解析传入的JSON参数
            var inputParams = JsonSerializer.Deserialize<dynamic>(args[0]);
            
            // 处理业务逻辑
            string result = "C# processed: " + inputParams;
            
            // 返回处理结果
            Console.WriteLine(result);
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Error: {ex.Message}");
        }
    }
}