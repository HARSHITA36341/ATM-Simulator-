{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d4b045c6-91ff-4e2d-951d-b6a01b4337d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Hi, how can I help you?\n",
      "1. Create PIN\n",
      "2. Change PIN\n",
      "3. Check balance\n",
      "4. Withdraw money\n",
      "5. Exit\n",
      "\n",
      "Enter your choice:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using ATM.\n"
     ]
    }
   ],
   "source": [
    "class Atm:\n",
    "    def __init__(self):\n",
    "        self.pin = \"\"\n",
    "        self.balance = 0\n",
    "        self.menu()\n",
    "\n",
    "    def menu(self):\n",
    "        user_input = input(\"\"\"\n",
    "Hi, how can I help you?\n",
    "1. Create PIN\n",
    "2. Change PIN\n",
    "3. Check balance\n",
    "4. Withdraw money\n",
    "5. Exit\n",
    "\n",
    "Enter your choice: \"\"\")\n",
    "\n",
    "        if user_input == \"1\":\n",
    "            self.create_pin()\n",
    "        elif user_input == \"2\":\n",
    "            self.change_pin()\n",
    "        elif user_input == \"3\":\n",
    "            self.check_balance()\n",
    "        elif user_input == \"4\":\n",
    "            self.withdraw()\n",
    "        else:\n",
    "            print(\"Thank you for using ATM.\")\n",
    "            \n",
    "\n",
    "    def create_pin(self):\n",
    "        self.pin = input(\"Enter your PIN: \")\n",
    "        self.balance = int(input(\"Enter your initial balance: \"))\n",
    "        print(\"PIN created successfully.\")\n",
    "        self.menu()\n",
    "\n",
    "    def change_pin(self):\n",
    "        old_pin = input(\"Enter your current PIN: \")\n",
    "        if old_pin == self.pin:\n",
    "            self.pin = input(\"Enter your new PIN: \")\n",
    "            print(\"PIN changed successfully.\")\n",
    "        else:\n",
    "            print(\"Incorrect PIN.\")\n",
    "        self.menu()\n",
    "\n",
    "    def check_balance(self):\n",
    "        user_pin = input(\"Enter your PIN: \")\n",
    "        if user_pin == self.pin:\n",
    "            print(\"Your current balance is:\", self.balance)\n",
    "        else:\n",
    "            print(\"Incorrect PIN.\")\n",
    "        self.menu()\n",
    "\n",
    "    def withdraw(self):\n",
    "        user_pin = input(\"Enter your PIN: \")\n",
    "        if user_pin == self.pin:\n",
    "            amount = int(input(\"Enter amount to withdraw: \"))\n",
    "            if amount <= self.balance:\n",
    "                self.balance -= amount\n",
    "                print(\"Withdrawal successful.\")\n",
    "                print(\"Remaining balance:\", self.balance)\n",
    "            else:\n",
    "                print(\"Insufficient balance.\")\n",
    "        else:\n",
    "            print(\"Incorrect PIN.\")\n",
    "        self.menu()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    Atm()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01fbc20c-25a5-4e76-93ff-c4b630efa534",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
