class Solution {
public:
    int countSegments(string s) {
        int count = 0;
        bool ischar = false;
        for (auto& i: s) {
            if (i != ' ') 
                ischar = true;
            else if ((i == ' ') && (ischar)) {
                count++;
                ischar = false;
            }
        }
        if (!ischar) 
            return count;
        else 
            return count+1;
    }
};