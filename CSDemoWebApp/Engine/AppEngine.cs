using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace CSDemoWebApp.Engine
{
    public class EngineException : Exception
    {
        public EngineException()
        {
        }
    }
    public class AppEngine
    {

        public static float Add(string num1, string num2)
        {
            float num1_float = 0, num2_float = 0;
            bool parsed_num1 = float.TryParse(num1, out num1_float);
            bool parsed_num2 = float.TryParse(num2, out num2_float);
            if (parsed_num1 && parsed_num2)
            {
                return (num1_float + num2_float);
            }
            throw new EngineException();
        }
        public static float Subtract(string num1, string num2)
        {
            float num1_float = 0, num2_float = 0;
            bool parsed_num1 = float.TryParse(num1, out num1_float);
            bool parsed_num2 = float.TryParse(num2, out num2_float);
            if (parsed_num1 && parsed_num2)
            {
                return (num1_float - num2_float);
            }
            throw new EngineException();
        }
        public static float Multiply(string num1, string num2)
        {
            float num1_float = 0, num2_float = 0;
            bool parsed_num1 = float.TryParse(num1, out num1_float);
            bool parsed_num2 = float.TryParse(num2, out num2_float);
            if (parsed_num1 && parsed_num2)
            {
                return (num1_float * num2_float);
            }
            throw new EngineException();
        }
        public static float Divide(string num1, string num2)
        {
            float num1_float = 0, num2_float = 0;
            bool parsed_num1 = float.TryParse(num1, out num1_float);
            bool parsed_num2 = float.TryParse(num2, out num2_float);
            if (parsed_num1 && parsed_num2 && 0 != num2_float)
            {
                return (num1_float / num2_float);
            }
            throw new EngineException();
        }
    }
}