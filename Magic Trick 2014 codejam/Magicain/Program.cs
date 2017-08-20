using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;

namespace Magicain
{
    class Program
    {
        public static StreamReader infile = new System.IO.StreamReader("C:/Users/Anu Chawla/Desktop/A-small-practice.in");
        public static string magic()
        {
            //declerations

            string toReturn =  "";
            string[] firstRow = new string[4];
            string[] secondRow = new string[4];
            string[] thirdRow = new string[4];
            string[] fourthRow = new string[4];
            string[] SelectedRow = new string[4];
            string[] SelectedRow2 = new string[4];
            bool didSplit = false;
            bool didSplit1 =  false;
            bool didSplit2 = false;
            bool didSplit3 = false;
            int selectedWithCard;
            bool did = false;

            selectedWithCard = Int32.Parse(infile.ReadLine());
            string dict = infile.ReadLine();
            if(didSplit == false)
            {
                firstRow = dict.Split(' ');
                didSplit = true;
            }
            dict = infile.ReadLine();
            if (didSplit1 == false)
            {
                secondRow = dict.Split(' ');
                didSplit1 = true;
            }
            dict = infile.ReadLine();
            if (didSplit2 == false)
            {
                thirdRow = dict.Split(' ');
                didSplit2 = true;
            }
            dict = infile.ReadLine();
            if (didSplit3 == false)
            {
                fourthRow = dict.Split(' ');
                didSplit = true;
            }
            if(selectedWithCard == 1)
            {
                SelectedRow = firstRow;
            }
            if (selectedWithCard == 2)
            {
                SelectedRow = secondRow;
            }
            if (selectedWithCard == 3)
            {
                SelectedRow = thirdRow;
            }
            if (selectedWithCard == 4)
            {
                SelectedRow = fourthRow;
            }
            didSplit = false;
            didSplit1= false;
            didSplit2= false;
            didSplit3 = false;
            selectedWithCard = Int32.Parse(infile.ReadLine());
            dict = infile.ReadLine();
            if (didSplit == false)
            {
                firstRow = dict.Split(' ');
                didSplit = true;
            }
            dict = infile.ReadLine();
            if (didSplit1 == false)
            {
                secondRow = dict.Split(' ');
                didSplit1 = true;
            }
            dict = infile.ReadLine();
            if (didSplit2 == false)
            {
                thirdRow = dict.Split(' ');
                didSplit2 = true;
            }
            dict = infile.ReadLine();
            if (didSplit3 == false)
            {
                fourthRow = dict.Split(' ');
                didSplit3 = true;
            }
            if (selectedWithCard == 1)
            {
                SelectedRow2 = firstRow;
            }
            if (selectedWithCard == 2)
            {
                SelectedRow2 = secondRow;
            }
            if (selectedWithCard == 3)
            {
                SelectedRow2 = thirdRow;
            }
            if (selectedWithCard == 4)
            {
                SelectedRow2 = fourthRow;
            }
            int matchingNumbrs = 0;
           
            int solution = 0;
            for (int x = 0; x < 4; x++)
            {
                if (SelectedRow2.Contains(SelectedRow[x]))
                {
                   
                    matchingNumbrs++;
                    solution = Int32.Parse(SelectedRow[x]);
                }
            }
            if(matchingNumbrs == 0)
            {
                toReturn = "Volunteer cheated!";
            }
            else if(matchingNumbrs == 1)
            {
                toReturn = (solution + "" );
            }
            else if(matchingNumbrs > 1)
            {
                toReturn = "Bad magician!";
            }

            return toReturn;
        }
        static void Main(string[] args)
        {
            StreamWriter output = new System.IO.StreamWriter("Output.txt");
            int cases = Int32.Parse(infile.ReadLine());
            for (int i = 1; i < cases+1; i++)
            {
                //magic();
                output.WriteLine("Case #" + i + ": " + magic());    
            }
            output.Flush();
            output.Close();
        }
    }
}
