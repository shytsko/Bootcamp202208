using System.Net.Sockets;
using System.Text;

var client = new TcpClient("127.0.0.1", 33333);
var sWriter = new StreamWriter(client.GetStream(), Encoding.UTF8);
var sReader = new StreamReader(client.GetStream(), Encoding.UTF8);




while (true)
{
    Console.Write("> ");
    string message = Console.ReadLine();
    sWriter.WriteLine(message);
    sWriter.Flush();
}
