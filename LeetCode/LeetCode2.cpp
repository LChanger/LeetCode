/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int x,y,cf,sum;
        cf=0;
        ListNode preHead(0), *p = &preHead;
        while(l1!=NULL||l2!=NULL)
        {
        	x=l1?l1->val:0;
       		y=l2?l2->val:0;
       		sum=x+y+cf;
       		cf=sum/10;
       		p->next=new ListNode(sum%10);
       		p=p->next;
       		l1=l1?l1->next:0;
       		l2=l2?l2->next:0;
        }
        return preHead.next;
    }
    int main(int argc, char const *argv[])
    {
    	/* code */
    	cout<<"nihao"<<endl;
    	return 0;
    }
};
