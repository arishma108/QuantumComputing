{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtyQa41g9BwAwnV2LAFZVP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/arishma108/QuantumComputing/blob/master/IBM%20Quantum%20Challenge%202024/util.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D84OvcvtIgDp",
        "outputId": "5ae1982f-74e2-413d-b990-fcc2f2f025ae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting qiskit\n",
            "  Downloading qiskit-1.1.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.3/4.3 MB\u001b[0m \u001b[31m16.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting rustworkx>=0.14.0 (from qiskit)\n",
            "  Downloading rustworkx-0.14.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.1/2.1 MB\u001b[0m \u001b[31m68.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: numpy<3,>=1.17 in /usr/local/lib/python3.10/dist-packages (from qiskit) (1.25.2)\n",
            "Requirement already satisfied: scipy>=1.5 in /usr/local/lib/python3.10/dist-packages (from qiskit) (1.11.4)\n",
            "Requirement already satisfied: sympy>=1.3 in /usr/local/lib/python3.10/dist-packages (from qiskit) (1.12.1)\n",
            "Collecting dill>=0.3 (from qiskit)\n",
            "  Downloading dill-0.3.8-py3-none-any.whl (116 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m116.3/116.3 kB\u001b[0m \u001b[31m13.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.8.0 in /usr/local/lib/python3.10/dist-packages (from qiskit) (2.8.2)\n",
            "Collecting stevedore>=3.0.0 (from qiskit)\n",
            "  Downloading stevedore-5.2.0-py3-none-any.whl (49 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.7/49.7 kB\u001b[0m \u001b[31m5.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: typing-extensions in /usr/local/lib/python3.10/dist-packages (from qiskit) (4.12.1)\n",
            "Collecting symengine>=0.11 (from qiskit)\n",
            "  Downloading symengine-0.11.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (39.4 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m39.4/39.4 MB\u001b[0m \u001b[31m14.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.0->qiskit) (1.16.0)\n",
            "Collecting pbr!=2.1.0,>=2.0.0 (from stevedore>=3.0.0->qiskit)\n",
            "  Downloading pbr-6.0.0-py2.py3-none-any.whl (107 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m107.5/107.5 kB\u001b[0m \u001b[31m12.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: mpmath<1.4.0,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy>=1.3->qiskit) (1.3.0)\n",
            "Installing collected packages: symengine, rustworkx, pbr, dill, stevedore, qiskit\n",
            "Successfully installed dill-0.3.8 pbr-6.0.0 qiskit-1.1.0 rustworkx-0.14.2 stevedore-5.2.0 symengine-0.11.0\n"
          ]
        }
      ],
      "source": [
        "!pip install qiskit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from qiskit import transpile, QuantumCircuit\n",
        "\n",
        "def version_check():\n",
        "    import qiskit\n",
        "    if qiskit.version.VERSION == '1.0.2':\n",
        "        return print(\"You have the right version! Enjoy the challenge!\")\n",
        "    else:\n",
        "        return print(\"please install right version by copy/paste and execute - !pip install 'qiskit[visualization]' == 1.0.2'\")\n",
        "\n",
        "def transpile_scoring(circ, layout, backend):\n",
        "\n",
        "    \"\"\"\n",
        "    A custom cost function that includes T1 and T2 computed during idle periods\n",
        "\n",
        "    Parameters:\n",
        "        circ (QuantumCircuit): circuit of interest\n",
        "        layouts (list of lists): List of specified layouts\n",
        "        backend (IBMQBackend): An IBM Quantum backend instance\n",
        "\n",
        "    Returns:\n",
        "        list: Tuples of layout and cost\n",
        "    \"\"\"\n",
        "\n",
        "    fid = 1\n",
        "\n",
        "    touched = set()\n",
        "    dt = backend.dt\n",
        "    num_qubits = backend.num_qubits\n",
        "\n",
        "    error=0\n",
        "\n",
        "    t1s = [backend.qubit_properties(qq).t1 for qq in range(num_qubits)]\n",
        "    t2s = [backend.qubit_properties(qq).t2 for qq in range(num_qubits)]\n",
        "\n",
        "\n",
        "    for item in circ._data:\n",
        "        for gate in backend.operation_names:\n",
        "            if item[0].name == gate:\n",
        "                if (item[0].name == 'cz') or (item[0].name == 'ecr'):\n",
        "                    q0 = circ.find_bit(item[1][0]).index\n",
        "                    q1 = circ.find_bit(item[1][1]).index\n",
        "                    fid *= 1 - backend.target[item[0].name][(q0, q1)].error\n",
        "                    touched.add(q0)\n",
        "                    touched.add(q1)\n",
        "                elif item[0].name == 'measure':\n",
        "                    q0 = circ.find_bit(item[1][0]).index\n",
        "                    fid *= 1 - backend.target[item[0].name][(q0, )].error\n",
        "                    touched.add(q0)\n",
        "\n",
        "                elif item[0].name == 'delay':\n",
        "                    q0 = circ.find_bit(item[1][0]).index\n",
        "                    # Ignore delays that occur before gates\n",
        "                    # This assumes you are in ground state and errors\n",
        "                    # do not occur.\n",
        "                    if q0 in touched:\n",
        "                        time = item[0].duration * dt\n",
        "                        fid *= 1-qubit_error(time, t1s[q0], t2s[q0])\n",
        "                else:\n",
        "                    q0 = circ.find_bit(item[1][0]).index\n",
        "                    fid *= 1 - backend.target[item[0].name][(q0, )].error\n",
        "                    touched.add(q0)\n",
        "\n",
        "    return fid\n",
        "\n",
        "\n",
        "def qubit_error(time, t1, t2):\n",
        "    \"\"\"Compute the approx. idle error from T1 and T2\n",
        "    Parameters:\n",
        "        time (float): Delay time in sec\n",
        "        t1 (float): T1 time in sec\n",
        "        t2 (float): T2 time in sec\n",
        "    Returns:\n",
        "        float: Idle error\n",
        "    \"\"\"\n",
        "    t2 = min(t1, t2)\n",
        "    rate1 = 1/t1\n",
        "    rate2 = 1/t2\n",
        "    p_reset = 1-np.exp(-time*rate1)\n",
        "    p_z = (1-p_reset)*(1-np.exp(-time*(rate2-rate1)))/2\n",
        "    return p_z + p_reset"
      ],
      "metadata": {
        "id": "sPiKrxgbI4gY"
      },
      "execution_count": 3,
      "outputs": []
    }
  ]
}