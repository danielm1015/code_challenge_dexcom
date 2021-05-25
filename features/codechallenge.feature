Feature: Dexcom Coding Challenge

    Scenario: Login to Dexcom CLARITY
        Given we are on "https://clarity.dexcom.com/"
        When user "codechallenge" logs in
        Then user is authorized

    # Scenario: Session Analysis
    #     Given "clarity.dexcom.com/" endpoint
    #     When post to call 
    #     Then analysis in None

