I did the following experiments.
1. Access supabase db on local machine
2. Access supabase db on cluster
3. Access supabase db through optuna on cluster login node
4. Access supabase db through optuna on multiple compute nodes simultaneously
	1. Problem: supabase limits the number of concurrent connections to 15
	2. Solution: use transaction pooler connections instead, and ask Chat for an optuna version that doesn't fail if it gets rejected and waits until a connection is free instead (it basically tries to write the result)
		1. Create a new version that uses ask/tell optuna, runs the file, and then keeps on trying to write until it finishes
		2. Make it work with pruning, with a toy pruning model
5. Run a CleanRL file, creating an objective function for it and then making sure it works
6. Run multiple batches at once, with CleanRL, and make sure it works.
7. Check resource allocation, and learn how to modify based on what is and isn't being used.