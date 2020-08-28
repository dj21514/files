
class Node {
public:
	int data;
	Node* next;
};

int main()
{
	Node n1;
	Node n2;
	Node n3;
	Node head;
	
	n1.next=&n2;
	n2.next=&n3;
	n3.next=nullptr;
	head = n1;
	return 0;
}