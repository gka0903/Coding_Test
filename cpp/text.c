#include <stdio.h>

int isPrime(int n)
{
    int i;
    if (n < 2)
    {
        return 0; 
    }
    for (i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}


int main(void)
{
    freopen("input.txt", "r", stdin);
    
    // (선택 사항) 만약 출력도 파일로 저장해야 한다면
    // "output.txt" 파일을 쓰기 모드("w")로 열고, 표준 출력(stdout)으로 사용
    freopen("output.txt", "w", stdout); 
    // ======================================

    int T, n, i, k;
    int j; 

    scanf("%d", &T);

    for (j = 0; j < T; j++)
    {
        scanf("%d", &n);

        for (i = n; i >= 2; i--)
        {
            if (isPrime(i) == 1)
            {
                k = i;   
                break; 
            }
        }

        printf("%d\n", k);
    }
    
    return 0; 
}