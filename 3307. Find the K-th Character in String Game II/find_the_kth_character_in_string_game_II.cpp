//Brute-Force
//T.C.->O(2^n)
//S.C.->O(2^n)
class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        string s = "a";
        for (int op : operations) {
            string t;
            if (op == 0) 
                t = s;
            else
                for (char c : s) 
                    t += (c == 'z' ? 'a' : c + 1);
            s += t;
        }
        return s[k - 1];
    }
};

//Optimal
//T.C.->O(n)
//S.C.->O(1)
class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int shift = 0;
        k--;
        
        for(int i = operations.size() - 1; i >= 0; i--) {
            long long half;
            if(i >= 60) {
                half = LLONG_MAX;
            } else {
                half = 1LL << i;
            }
            
            if(k >= half) {
                k -= half;
                shift += operations[i];
            }
        }
        
        return (char)('a' + shift % 26);
    }
};
