#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int create_account();
int login();

struct account_details
{
    char username[10];
    char password[13];
    int num_of_sub;
    char subs[10][15];
}acc;

int create_account()
{
    printf("\n\n\n\t\t\t\t\t  ||||CREATE ACCOUNT||||\n\n");
    int x;
    FILE *fp2;
    printf("Enter the username:");
    scanf("%s",&acc.username);
    printf("Enter the password:");
    scanf("%s",&acc.password);
    printf("Number of subjects:");
    scanf(" %d",&acc.num_of_sub);
    printf("Enter the name of subjects:\n");
    for(int i=0;i<acc.num_of_sub;i++)
    {
        printf("%d)",i+1);
        scanf("%s",acc.subs[i]);
    }
    fp2=fopen("new.txt","w");
    x=fwrite(&acc,sizeof(acc),1,fp2);
    if(x==1)
    {
        printf("\n\t\t\tThank You! Account Created Successfully! Continue to Login!\n");
        fclose(fp2);
        return login();

    }
    else
    {
        printf("Account creation failed! please try again!");
        fclose(fp2);
        return create_account();
    }
    fclose(fp2);
    
}
int login()
{
    // to be coded later
    printf("TBA");
}

void menu1()
{
    int choice;
    printf("\n\n\t\t\t\t\t||||STUDY PLANNER APPLICATION||||\t\t\t\n\n1) Create Account \n2)Login\n3)Exit\nEnter your choice:");
    scanf("%d",&choice);
    if(choice==1)
    {
        create_account();
    }
    else if(choice==2)
    {
        login();
    }
    else if(choice==3)
    {
        printf("");
    }

}

int main()
{
    menu1();
    //display();
    //daily_planner();
    
}