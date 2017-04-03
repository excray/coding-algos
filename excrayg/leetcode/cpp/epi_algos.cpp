#include <iostream>
using namespace std;
#include <cstring>
#include <map>
#include <utility>
#include <vector>

template<typename T>
struct Node{
	T data;
	Node<T>* next; 
	Node<T>(T _a):data(_a), next(NULL){}

	static void printList(Node<T>* a)
	{
		while(a != NULL)
		{
			cout<<a->data<<"->";
			a = a->next;
		}
		cout<<endl;
	}

	static void addList(Node<T>* a1, Node<T>* a2)
	{
		T carry=(T)0, sum;
		Node<T>* prev = NULL, *head = NULL, *rem;
		if(!a1)
			printList(a2);
		if(!a2)
			printList(a1);
		printList(a1);
		printList(a2);

		while(a1 && a2)
		{
			sum = (a1->data+a2->data+carry);
			cout<<sum<<endl;
			carry = sum / 10;
			sum %= 10;
			if(prev)
			{
				Node<T>* n = new Node<T>(sum);
				prev->next = n;
				prev = n;
			}
			else
			{
				Node<T>* n = new Node<T>(sum);
				prev = n;
				head = prev;
			}
			a1 = a1->next; a2 = a2->next;
		}
		// printList(head);

		a1?rem=a1:rem=a2;
		while(rem)
		{
			sum = (rem->data+carry);
			carry = sum / 10;
			sum %= 10;
			Node<T>* n = new Node<T>(sum);
			prev->next = n;
			prev = n;
			rem = rem->next;
		}
		if(carry)
		{
			Node<T>* n = new Node<T>(carry);
			prev->next = n;
		}

		printList(head);

	}

	static void mergeList(Node<T>* a1, Node<T>* a2)
	{
		
		Node<T>* head1 = a1;
		Node<T>* head2 = a2;

		Node<T>* prev = NULL, *head=NULL;
		while(head1 && head2)
		{
			cout<<head1->data<<" "<<head2->data<<endl;
			if(head1->data < head2->data)
			{
				if(!head)
					head = head1;
				if(prev)
				{
					prev->next = head1;
				}
				prev = head1;
				head1 = head1->next;
			}
			else
			{

				if(!head)
					head = head2;
				if(prev)
				{
					prev->next = head2;
				}
				prev = head2;
				head2 = head2->next;
			}
		}
		cout<<"Merged\n";
		if(head1)
			prev->next = head1;
		if(head2)
			prev->next = head2;

		printList(head);
	}

	static void reverseList(Node<T>* head)
	{
		Node<T>* curr = head, *prev = NULL;
		while( curr != NULL )
		{
			Node<T>* temp = curr->next;
			if(prev)
			{
				curr->next = prev;
				prev = curr;
				curr = temp;
			}
			else
			{
				prev = curr;
				prev->next = NULL;
				curr = temp;
			}
		}
		printList(prev);
	}

	static void findOverlappintg(Node<T>* head, Node<T>* tail)
	{

	}

	// static void reverseSubList(Node<T>* head, int s, int f)
	// {
	// 	Node<T>* curr = head, *prev = NULL, *list_prev = NULL, *list_curr = NULL;
	// 	int ctr = 1;
	// 	while( curr != NULL )
	// 	{
	// 		if( ctr > s && ctr <= f)
	// 		{
	// 			if(!list_prev)
	// 				list_prev = prev;
	// 			if(!list_curr)
	// 				list_curr = curr;
	// 			Node<T>* temp = curr->next;
	// 			if(prev)
	// 			{
	// 				curr->next = prev;
	// 				prev = curr;
	// 				curr = temp;
	// 			}
	// 			else
	// 			{
	// 				prev = curr;
	// 				prev->next = NULL;
	// 				curr = temp;
	// 			}
	// 		}
	// 		else if( ctr <= s)
	// 		{
	// 			list_prev = prev;
	// 			prev = curr;
	// 			curr = curr->next;
	// 		}
	// 		else
	// 		{
	// 			list_prev->next = prev;
	// 			list_curr-next = curr;
	// 			break;
	// 		}
	// 		ctr++;
	// 	}
	// 	printList(head);
	// }

	// static void reverseKList(Node<T>* head, int k)
	// {

	// }


};


template <typename t>
class Queue
{
	public:
		Queue(t max):max1(max){}
		void Enqueue(t data)
		{
			//if(data>max) max = data;
			a.push_back(make_pair<t,t>(data, 1));
		}
		t Dequeue()
		{
			if(!b.empty())
			{
				pair<t, t> p = b.back(); b.pop_back();

				return p.first;
			}
			else
			{
				t max = max1;
				while(!a.empty())
				{
					t p = a.back().first; a.pop_back();
					if(p > max) max = p;
					b.push_back(make_pair<t,t>(p, max));
				}
				if(!b.empty())
				{
					t r =  b.back().first;
					b.pop_back();
					return r;
				}
				else
				{
					cout<<"Queue is empty\n";
				}
			}
		}
		t getMax()
		{

			if(!b.empty())
			{
				pair<t, t> p = b.back(); b.pop_back();
				b.push_back(p);
				return p.second;
			}
			else
			{
				t max = max1;
				while(!a.empty())
				{
					t p = a.back().first; a.pop_back();
					if(p > max) max = p;
					b.push_back(make_pair<t,t>(p, max));
				}
				if(!b.empty())
				{
					pair<t, t> p = b.back(); b.pop_back();
					b.push_back(p);
					return p.second;
				}
				else
				{
					cout<<"Max: Queue is empty\n";
				}
			}
		}

	private:
		vector<pair<t,t> > a;
		vector<pair<t,t> > b;
		t max1;

};



int main(int argc, char const *argv[])
{
	
	// char* s = "bbaacd";
	// replaceAndDelete(s);
	Node<int>* a1 = new Node<int>(9);
	Node<int>* a2 = new Node<int>(9);
	Node<int>* a3 = new Node<int>(9);
	Node<int>* a4 = new Node<int>(9);
	Node<int>* a5 = new Node<int>(9);

	a1->next = a2;
	a2->next = a3;
	a4->next = a5;


	Node<int>::printList(a1);
	Node<int>::printList(a4);

	// printList<int>(a1);
	//Node<int>::mergeList(a1, a4);
	//Node<int>::reverseList(a1);

	cout<<"addList\n";
	Node<int>::printList(a1);
	Node<int>::printList(a4);
	Node<int>::addList(a1,a4);


	cout<<"Queue\n";
	Queue<int> q(-1000);
	q.Enqueue(5);
	q.Enqueue(1);
	q.Enqueue(2);
	cout<<"\n"<<q.Dequeue()<<"\n";
	cout<<"\n"<<q.getMax()<<"\n";
	cout<<"\n"<<q.Dequeue()<<"\n";

	return 0;
}