//T.C.->O(n*k)
//S.C.->O(n+k)
class Solution {
public:
    int possibleStringCount(string word, int k) {
        int n = word.size();
        if (k == n) return 1;
        if (k > n) return 0;

        const int MOD = 1e9 + 7;
        vector<int> groups;
        
        // Step 1: Group consecutive same characters
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && word[j] == word[i]) j++;
            int len = j - i;
            k--; // you spend 1 move to split each group
            if (len > 1) {
                groups.push_back(len - 1);  // store extra possible splits
            }
            i = j;
        }

        k = max(0, k);

        // Step 2: Multiply all (group + 1) to get base answer
        long long answer = 1;
        for (int g : groups) {
            answer = (answer * (g + 1)) % MOD;
        }

        // Step 3: Handle simple k cases
        if (k == 0) return answer;
        if (k == 1) return (answer - 1 + MOD) % MOD;
        if (k == 2) return (answer - 1 - (int)groups.size() + MOD) % MOD;

        // Step 4: DP when k > 2
        vector<long long> prev_dp(k, 0);
        prev_dp[0] = 1;

        for (int group_size : groups) {
            vector<long long> dp(k, 0);
            long long window_sum = 0;
            for (int i = 0; i < k; ++i) {
                window_sum += prev_dp[i];
                if (i - group_size - 1 >= 0) {
                    window_sum -= prev_dp[i - group_size - 1];
                }
                window_sum = (window_sum + MOD) % MOD;
                dp[i] = window_sum;
            }
            prev_dp = dp;
        }

        long long subtract = 0;
        for (int i = 0; i < k; ++i) {
            subtract = (subtract + prev_dp[i]) % MOD;
        }

        return (answer - subtract + MOD) % MOD;
    }
};
