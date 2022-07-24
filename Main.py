from blockfrost import BlockFrostApi, ApiError, ApiUrls
import requests

api = BlockFrostApi(
    project_id='mainnetu1rPvSktZ6D9L02yXJVIPrfQytMLNqvI'
    
)
try:
    health = api.health()
    print(health)
    health = api.health(return_type="json")
    print(health)
    health = api.health(return_type='pandas')
    print(health)
    
    account_rewards = api.account_rewards(
        stake_address='stake1u9wn7nqwdpve8ta5p3gzw873kkn5c007ndlqtpyaefsdjcsfldvjl',
        count=20,     
    )
    print(account_rewards[0].epoch)
    print(len(account_rewards))
    account_rewards = api.account_rewards(
        stake_address='stake1u9wn7nqwdpve8ta5p3gzw873kkn5c007ndlqtpyaefsdjcsfldvjl',
        count=20,
        gather_pages=True
    )
    print(account_rewards[0].epoch)
    print(len(account_rewards))

    address = api.address(
        address = 'addr1q8swkv43fr8ygz29mvxss2edmh4grs2j6a9ewcm7y8y0sgja8axqu6zejwhmgrzsyu0ardd8fs7laxm7qkzfmjnqm93q5mzmvh',)
    print(address.type)
    #for amount in address.amount:
      #  print(amount.unit)
   
    
except ApiError as e:
    print(e)



 