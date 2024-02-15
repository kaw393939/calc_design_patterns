# test_main.py
import main

def test_hello_world(capfd):
    main.main()  # Call the main function directly
    out, err = capfd.readouterr()
    assert out == "Hello World\n"
