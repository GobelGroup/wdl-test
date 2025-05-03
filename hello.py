from prefect import flow, task

@flow(name='Testing',log_prints=True)
def main():
    print('hello world test 3')

#main()
