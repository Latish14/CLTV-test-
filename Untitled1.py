{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJ5uLUekS3EwOmc9UGavLX",
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
        "<a href=\"https://colab.research.google.com/github/Latish14/CLTV-test-/blob/main/Untitled1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n",
        "!pip install lifetimes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kJdaTi3zz8Ly",
        "outputId": "e1b987c3-0de2-4706-9537-1d4579650271"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.44.1-py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.4)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.13.1)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.33.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.24.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.44.1-py3-none-any.whl (9.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.8/9.8 MB\u001b[0m \u001b[31m60.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m93.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.44.1 watchdog-6.0.0\n",
            "Collecting lifetimes\n",
            "  Downloading Lifetimes-0.11.3-py3-none-any.whl.metadata (4.8 kB)\n",
            "Requirement already satisfied: numpy>=1.10.0 in /usr/local/lib/python3.11/dist-packages (from lifetimes) (2.0.2)\n",
            "Requirement already satisfied: scipy>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from lifetimes) (1.14.1)\n",
            "Requirement already satisfied: pandas>=0.24.0 in /usr/local/lib/python3.11/dist-packages (from lifetimes) (2.2.2)\n",
            "Requirement already satisfied: autograd>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from lifetimes) (1.7.0)\n",
            "Collecting dill>=0.2.6 (from lifetimes)\n",
            "  Downloading dill-0.3.9-py3-none-any.whl.metadata (10 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.24.0->lifetimes) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.24.0->lifetimes) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.24.0->lifetimes) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas>=0.24.0->lifetimes) (1.17.0)\n",
            "Downloading Lifetimes-0.11.3-py3-none-any.whl (584 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m584.2/584.2 kB\u001b[0m \u001b[31m9.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dill-0.3.9-py3-none-any.whl (119 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m119.4/119.4 kB\u001b[0m \u001b[31m9.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: dill, lifetimes\n",
            "Successfully installed dill-0.3.9 lifetimes-0.11.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RQ2jdqkBzuD_",
        "outputId": "37560743-1713-49e4-c477-87bfde0d5955"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-04-11 12:25:54.664 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.669 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.981 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-04-11 12:25:54.985 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.987 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.989 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.989 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.994 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-04-11 12:25:54.996 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "from lifetimes import BetaGeoFitter, GammaGammaFitter\n",
        "from lifetimes.utils import summary_data_from_transaction_data, calibration_and_holdout_data\n",
        "\n",
        "st.set_page_config(page_title=\"CLV Predictor\", layout=\"wide\")\n",
        "st.title(\"📊 Customer Lifetime Value (CLV) Predictor\")\n",
        "\n",
        "uploaded_file = st.file_uploader(\"Upload transaction CSV file\", type=[\"csv\"])\n",
        "\n",
        "if uploaded_file:\n",
        "    try:\n",
        "        df = pd.read_csv(uploaded_file, encoding='latin-1')\n",
        "\n",
        "        # Preprocessing\n",
        "        df.dropna(subset=['CustomerID', 'InvoiceDate', 'Quantity', 'UnitPrice'], inplace=True)\n",
        "        df.drop_duplicates(inplace=True)\n",
        "        df = df[df['Quantity'] > 0]\n",
        "        df = df[df['UnitPrice'] > 0]\n",
        "        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')\n",
        "        df['CustomerID'] = df['CustomerID'].astype(int)\n",
        "        df['TotalPrice'] = df['Quantity'] * df['UnitPrice']\n",
        "\n",
        "        # Summarize transaction data\n",
        "        summary = summary_data_from_transaction_data(df, 'CustomerID', 'InvoiceDate', 'TotalPrice')\n",
        "\n",
        "        # Remove customers with no monetary value (required by Gamma-Gamma model)\n",
        "        summary = summary[summary['monetary_value'].notnull() & (summary['monetary_value'] > 0)]\n",
        "\n",
        "        # Modeling\n",
        "        bgf = BetaGeoFitter(penalizer_coef=0.1)\n",
        "        bgf.fit(summary['frequency'], summary['recency'], summary['T'])\n",
        "\n",
        "        ggf = GammaGammaFitter(penalizer_coef=0.0)\n",
        "        ggf.fit(summary['frequency'], summary['monetary_value'])\n",
        "\n",
        "        # Predictions with NaN-safe conversion\n",
        "        predicted_purchases = bgf.conditional_expected_number_of_purchases_up_to_time(\n",
        "            90, summary['frequency'], summary['recency'], summary['T']\n",
        "        )\n",
        "        summary['predicted_purchases'] = predicted_purchases.fillna(0).round().astype(int)\n",
        "\n",
        "        summary['predicted_monetary'] = ggf.conditional_expected_average_profit(\n",
        "            summary['frequency'], summary['monetary_value']\n",
        "        ).fillna(0)\n",
        "\n",
        "        summary['CLV'] = ggf.customer_lifetime_value(\n",
        "            bgf, summary['frequency'], summary['recency'],\n",
        "            summary['T'], summary['monetary_value'], time=24, discount_rate=0.0\n",
        "        ).fillna(0)\n",
        "\n",
        "        # Show predictions\n",
        "        st.subheader(\"CLV Predictions Table\")\n",
        "        st.write(summary[['predicted_purchases', 'predicted_monetary', 'CLV']].head(10))\n",
        "\n",
        "        # Plotting\n",
        "        st.subheader(\"CLV Distribution Plot\")\n",
        "        clv_filtered = summary[summary['CLV'] < 10000]['CLV']\n",
        "        p25, p50, p75 = np.percentile(clv_filtered, [25, 50, 75])\n",
        "\n",
        "        fig, ax = plt.subplots(figsize=(10, 6))\n",
        "        sns.histplot(clv_filtered, bins=50, kde=True, color='skyblue')\n",
        "        plt.axvline(p25, color='green', linestyle='--', label=f'25th %ile: {p25:.0f}')\n",
        "        plt.axvline(p50, color='blue', linestyle='--', label=f'50th %ile: {p50:.0f} (Median)')\n",
        "        plt.axvline(p75, color='red', linestyle='--', label=f'75th %ile: {p75:.0f}')\n",
        "        plt.legend()\n",
        "        ax.set_title(\"CLV Distribution\")\n",
        "        st.pyplot(fig)\n",
        "\n",
        "        # Optional Calibration Output\n",
        "        if st.checkbox(\"Show calibration/holdout summary\"):\n",
        "            calib_holdout = calibration_and_holdout_data(df, 'CustomerID', 'InvoiceDate',\n",
        "                                                        observation_period_end=df['InvoiceDate'].min() + pd.Timedelta(days=180),\n",
        "                                                        monetary_value_col='TotalPrice')\n",
        "            st.write(\"Calibration/Holdout Summary:\")\n",
        "            st.write(calib_holdout.head())\n",
        "\n",
        "    except Exception as e:\n",
        "        st.error(f\"⚠️ Error: {e}\")\n"
      ]
    }
  ]
}
