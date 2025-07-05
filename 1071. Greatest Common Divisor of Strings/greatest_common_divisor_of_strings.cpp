//T.C.=O(min(∣str1∣,∣str2∣)⋅(∣str1∣+∣str2∣))
//S.C.=O(|str1|+|str2|)
class Solution {
public:
    string gcdOfStrings(string str1, string str2)
    {
        int len1 = str1.length(), len2 = str2.length();
        auto isDivisor = [&](int l)
        {
            if (len1 % l != 0 || len2 % l != 0)
                return false;
            string pattern = str1.substr(0, l);
            string repeated1 = "", repeated2 = "";
            for (int i = 0; i < len1 / l; ++i)
                repeated1 += pattern;
            for (int i = 0; i < len2 / l; ++i)
                repeated2 += pattern;
            return (repeated1 == str1 && repeated2 == str2);
        };
        for (int l = min(len1, len2); l >= 1; --l) {
            if (isDivisor(l)) {
                return str1.substr(0, l);
            }
        }
        return "";
    }
};


//OR

//T.C.=S.C.=O(|str1|+|str2|)
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1)
      return "";
    const int g = gcd(str1.length(), str2.length());
    return str1.substr(0, g);
    }
};
