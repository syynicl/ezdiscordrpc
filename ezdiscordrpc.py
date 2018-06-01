try:
    # Import modules
    from pypresence import Presence
    import time

    # Connect to Discord
    cid = int(input('RPC Client ID: '))
    rpc = Presence(cid)
    rpc.connect()

    # Set RPC
    rpc.update(small_image = 'small', large_image = 'large')
    print('RPC set successfully.')

    # Update RPC every 15 seconds
    while True:
        time.sleep(15)

# Custom KeyboardInterrupt message
except KeyboardInterrupt:
    print('\nProgram stopped using Ctrl+C.')