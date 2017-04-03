
#include <iostream>
using namespace std;

bool finished = false;


bool is_a_solution(int* a, int k, int n)
{
	return k==n;
}

void construct_candidates_perm(int* a, int k, int n, int* c, int* ncandidates)
{
	int i;
	bool in_perm[1000];

	for(i = 1; i < 1000; i++) 
		in_perm[i] = false;

	for( i = 1; i < k; i++)
	{
		// if(a[i]==10000) cout<<"Whatt";
		in_perm[a[i]] = true;
		// cout<<i<<" "<<a[i]<<" ";
	}

	*ncandidates = 0;
	for(i = 1; i<=n; i++)
		if( in_perm[i] == false )
		{
			c[*ncandidates] = i;
			*ncandidates+=1;
		}
	cout<<*ncandidates<<endl;

}

void construct_candidates(int* a, int k, int n, int* c, int* ncandidates)
{
	c[0] = true;
	c[1] = false;
	*ncandidates = 2;
}

void process_solution_perm(int* a, int k, int n)
{
	int i;
	
	for(i = 1; i<=k; i++)
		cout<<" "<<a[i];
	cout<<endl;
}

void process_solution(int* a, int k, int n)
{
	int i;
	cout<<"{";
	for(i = 1; i<=k; i++)
		if(a[i] == true) cout<<" "<<i;
	cout<<"}"<<endl;
}


void backtrack(int *a, int k, int n)
{
	int c[10000];
	int ncandidates;
	int i;

	if(is_a_solution(a,k,n))
	{
		process_solution_perm(a,k,n);
	}
	else
	{
		k = k+1;
		construct_candidates_perm(a,k,n,c, &ncandidates);
		for(i=0; i<ncandidates; i++)
		{
			a[k] = c[i];
			//make move
			backtrack(a, k, n);
			//unmake move
			if(finished) return;
		}
	}
}

int main(int argc, char const *argv[])
{
	int a[100];
	int n = 4;
	backtrack(a, 0, n);
	return 0;
}