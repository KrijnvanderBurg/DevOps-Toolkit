az ad sp create-for-rbac --name "sp-terraform" --role Contributor --scopes /subscriptions/4111975b-f6ca-4e08-b7b6-87d7b6c35840
// to create resource locks, the role `user access administrator` is required.
az role assignment create --assignee 898709ce-d493-4991-8b2a-6772b0feb19a --role "User Access Administrator" --scope /subscriptions/4111975b-f6ca-4e08-b7b6-87d7b6c35840
