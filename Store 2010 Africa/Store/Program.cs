using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;

namespace Store
{
    class Program
    {
        public static StreamReader infile = new System.IO.StreamReader("C:/Users/Anu Chawla/Desktop/A-small-practice.in");
      
        //val 1 repersents the ammount of money that needs to be spent
        //val 2 repersents the amount of terms and use that in the for loop to get the prices
        public static string store(int val1, int val2, int debug)
        {
            string toReturn = "";
            bool didSplit = false;
            bool hasGone = false;
            int spending = val1;
            int terms = val2;
            string dict;
            string[] storage = new string[terms];
               
                dict = infile.ReadLine();
               
                if (didSplit == false)
                {   
                    storage = dict.Split(' ');
                    didSplit = true;
                }
            
            for (int u = 0; u < terms;)
            {
               

                int d = terms-1;
                while (d>=0)
                    {
                    if(Int32.Parse(storage[u])+Int32.Parse(storage[d]) == spending && (u == d) == false && hasGone == false)
                    {
                        

                         //   Console.WriteLine((u + 1) + " " + (d + 1));
                        //output.WriteLine((u + 1) + " " + (d + 1));
                        hasGone = true;
                        toReturn = (u + 1) + " " + (d + 1);
                        d--;

                    }
                    d--;

                }
                u++;

            }
            return toReturn;
        }
        static void Main(string[] args)
        {
                StreamWriter output = new System.IO.StreamWriter("Output.txt");

                int cases = Int32.Parse(infile.ReadLine());
            for(int i = 1; i < cases+1; i ++)
            {
                int spending =Int32.Parse(infile.ReadLine());
                int terms = Int32.Parse(infile.ReadLine());
                int cas = i;
                output.WriteLine("Case #" + i +": " + store(spending, terms, cas));
                
            }

                output.Flush();
                output.Close();
        }
    }
}
