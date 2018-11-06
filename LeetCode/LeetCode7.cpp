class Solution {
public:
    int reverse(int x) {
    	int y=0;
    	int temp=0;
        while(x>0)
        {
        	y*=10;
        	temp=x%10;
        	x/=10;
        	y=y+temp;
        }
        return y
    }
    int main(int argc, char const *argv[])
    {
    	/* code */
    	int x=123;
        t=new Solution();
    	printf("%d\n",t.reverse(x));
    	return 0;
    }
};