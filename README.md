# FindMaxAward
package com.homework;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Exercise16_13 {
	static JTextArea list;
	static JTextField txt_loan;
	static JTextField txt_years;

	public static void main(String[] args) {
		JFrame frame = new JFrame("Exercise16_13");
		frame.setSize(513, 315);
		frame.setLayout(null);
		JPanel com = new JPanel();
		com.setBounds(0, 0, 500, 30);
		com.setLayout(null);
		JLabel lbl_Loan = new JLabel("Loan Amount");
		lbl_Loan.setBounds(0, 0, 100, 30);
		txt_loan = new JTextField();
		txt_loan.setBounds(80, 0, 100, 30);
		JLabel lbl_years = new JLabel("number of years");
		lbl_years.setBounds(180, 0, 100, 30);
		txt_years = new JTextField();
		txt_years.setBounds(280, 0, 100, 30);
		JButton button = new JButton("show table");
		button.setBounds(380, 0, 100, 30);
		button.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				String output = "Interest Rage      Monthly Payment          Total Payment\n";
				double loan = Double.parseDouble(txt_loan.getText());
				double years = Double.parseDouble(txt_years.getText());
				for (double t = 5.0; t <= 8; t += 0.125) {
					double monthlyInteresRagte = t / 1200;
					double monthlyPayment = loan * monthlyInteresRagte
							/ (1 - 1 / Math.pow(1 + monthlyInteresRagte, years * 12));
					output += String.format("%-24.3f%-34.2f%-8.2f\n", t, monthlyPayment, (monthlyPayment * 12) * years);
				}
				list.setText(output);
			}
		});
		list = new JTextArea(50, 50);
		JScrollPane pane = new JScrollPane(list, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
				JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
		pane.setBounds(0, 30, 500, 250);
		com.add(lbl_Loan);
		com.add(txt_loan);
		com.add(lbl_years);
		com.add(txt_years);
		com.add(button);
		frame.add(com);
		frame.add(pane);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);

	}

}
