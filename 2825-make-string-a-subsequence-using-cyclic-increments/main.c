#include <string.h>
#include <stdbool.h>

typedef unsigned int uint;

bool canMakeSubsequence(char* str1, char* str2) {
    uint len1 = strlen(str1);
    uint len2 = strlen(str2);

    if (len2 > len1)
        return false;

    uint i = 0;
    uint j = 0;

    while (i < len1 && j < len2) {
        if ((str2[j] - str1[i] + 26) % 26 <= 1)
            ++j;
        ++i;
    }

    return j == len2;
}
