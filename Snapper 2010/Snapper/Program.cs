using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;


namespace Snapper
{
    class Program
    {
        public struct snap
        {
            public bool power;
            public bool toggle;
        }
        public static bool snapCounter(int snappers, int snaps)
            {
            snap[] arr = new snap[snappers];
            int i = snappers;
            int howmany = 0;
            i = 0;
                for (int z = 0; z < snaps; z++)
                {
                   
                    arr[0].power = true;
                int first = 1;
                while (first <= snappers - 1)
                {
                    if (arr[0].toggle == false)
                    {

                        arr[first].power = false;
                    }
                    first++;
                }
                    if (i > 0)
                    {
                        arr[0].power = true;
                        if (arr[i - 1].toggle == true && arr[i - 1].power == true)
                        {
                            arr[i].power = true;
                        }
                    }
                    if (arr[0].power == true)
                    {

                        arr[0].toggle = !arr[0].toggle;
                    }
                int second = 1;
              while (second <= snappers - 1)
                    {
                        if (arr[second].power == true)
                        {

                            arr[second].toggle = !arr[second].toggle;
                        }
                        second++;
                    }
                
                int third = 1;

                    while (third <= snappers - 1)
                    {
                        if (arr[third - 1].toggle == true && arr[third - 1].power == true)
                        {
                            arr[third].power = true;
                        }
                        third++;
                    }
                
                int last = 1;
                while(last<= snappers -1)
                {
                    if (arr[0].toggle == false)
                    {

                        arr[last].power = false;
                    }
                        last++;
                  
                    
                }
                if (i < snappers - 1)
                {

                    i++;
                }   
                howmany++;
                first = 1;
                second = 1;
                third = 1;
                last = 1;

            }
                if (arr[snappers-1].power == true && arr[snappers-1].toggle==true)
                {
                    return true;
                }
                else
                {
                    return false;
                }
        }

        static void Main(string[] args)
        {
            bool didSplit = false;
            StreamReader infile = new System.IO.StreamReader("C:/Users/Anu Chawla/Desktop/A-small-practice.in");
            StreamWriter output = new System.IO.StreamWriter("Output.txt");     
            int cases = Int32.Parse(infile.ReadLine());
            //Console.WriteLine(cases);
            String[] storage;
    
            int n;
            int k;
            string dict;
          
            for(int z = 1; z < cases+1; z++)
            {
                dict = infile.ReadLine();
                storage = dict.Split(' ');
                
                                if ( didSplit == false)
                                {
                                    storage = dict.Split(' ');
                                    didSplit = true;
                                }
                
                n = Int32.Parse(storage[0]);
                k = Int32.Parse(storage[1]);
                didSplit = false;
               //if(snapCounter(n,k) == true)
               //{
               //    output.WriteLine("Case #{0}        : ON", z);
               //}
               //else
               //{
               //    output.WriteLine("Case #{0}: OFF", z);
               //}
                //if (k % (n << 1) == 1)
                //{


                //    output.WriteLine("Case #{0}: ON", z);
                //}
                //else
                //{
                //    output.WriteLine("Case #{0}: OFF", z);
                //}
             }


            output.Flush();
            output.Close();
            snapCounter(6, 61);


        }


        }
    }

