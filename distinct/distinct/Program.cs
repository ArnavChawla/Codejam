using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;

namespace distinct
{
    class Program
    {
        // Declare the input file 
        public static  StreamReader infile = new System.IO.StreamReader("C:/Users/Arnav/Downloads/A-small-practice (1).in");
        public static String findDistinct()
        {
            
            String toReturn = "";
            // because we are checking values against eachother we have to declare both temporary and permanent  variables
            int largest = 0;
            int numOfDistinct = 0;
            String asd = infile.ReadLine();
            Console.WriteLine(asd);
            int names = Int32.Parse(asd);
            String name = "";
            String tempName;
            char[] tempArr;
            char[] existingChar = new char[100];
            List<char> chars = new List<char> { };
            for (int i = 0; i < names; i++)
            {
                tempName = infile.ReadLine();
                tempArr = tempName.ToCharArray();
                for(int j = 0; j < tempArr.Length; j++)
                {
                    char x = tempArr[j];
                    x = Char.ToLower(x);
                    if(!chars.Contains(x) && x != ' ')
                    {
                        numOfDistinct++;
                        chars.Add(x);
                    }
                }
                if (numOfDistinct >=largest)
                {
                    largest = numOfDistinct;
                    
                    name = tempName;
                }
                Console.WriteLine(numOfDistinct);
                numOfDistinct = 0;
                chars.Clear();
            }
            
            Console.WriteLine(name);
             toReturn = name;
            return toReturn;
            
        }
        static void Main(string[] args)
        {
            StreamWriter output = new System.IO.StreamWriter("Output.txt");
            int cases = Int32.Parse(infile.ReadLine());
            for (int i = 1; i <= cases; i++)
            {
                output.WriteLine("Case #{0}: {1}",i,findDistinct());
            }
            output.Flush();
            output.Close();
        }
    }
}
