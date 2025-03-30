from openai import OpenAI
import json

client = OpenAI(api_key='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')

class VulnerabilityClassifier:
    def classify(self, scan_results):
        prompt = f"""
        Classify the vulnerabilities from the given scan results into structured JSON including:
        - CVE IDs (if applicable)
        - CVSS Scores (if available)
        - Impact level
        - Short description
        - Remediation recommendations

        Scan Results:
        {scan_results}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content
