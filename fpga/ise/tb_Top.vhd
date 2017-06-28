--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   02:00:36 06/04/2015
-- Design Name:   
-- Module Name:   /home/daniel/hardware/OLALA/fpga/ise/tb_Top.vhd
-- Project Name:  olala
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: Top
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use IEEE.numeric_std.all;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY tb_Top IS
END tb_Top;
 
ARCHITECTURE behavior OF tb_Top IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT Top
    PORT(
         clk : IN  std_logic;
         cpuclock : OUT  std_logic;
         sysreset : IN  std_logic;
         button : IN  std_logic;
         notcpureset : INOUT  std_logic;
         notcpuhalt : INOUT  std_logic;
         notas : IN  std_logic;
         rnotw : IN  std_logic;
         notuds : IN  std_logic;
         notlds : IN  std_logic;
         dtack : OUT  std_logic;
         notbr : OUT  std_logic;
         notbg : IN  std_logic;
         addr : IN  unsigned(22 downto 0);
         data : INOUT unsigned(15 downto 0);
         notramcs : OUT  std_logic;
         ipl : OUT  unsigned(2 downto 0);
         notoe : OUT  std_logic;
         notuwe : OUT  std_logic;
         notlwe : OUT  std_logic;
         notberr : OUT  std_logic;
         leds : OUT  unsigned(7 downto 0);
         rx : IN  std_logic;
         tx : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal sysreset : std_logic := '0';
   signal button : std_logic := '0';
   signal notas : std_logic := '1';
   signal rnotw : std_logic := '1';
   signal notuds : std_logic := '1';
   signal notlds : std_logic := '1';
   signal notbg : std_logic := '1';
   signal addr : unsigned(22 downto 0) := (others => '0');
   signal rx : std_logic := '1';

	--BiDirs
   signal notcpureset : std_logic;
   signal notcpuhalt : std_logic;
   signal data : unsigned(15 downto 0);
   signal tx : std_logic;

 	--Outputs
   signal cpuclock : std_logic;
   signal dtack : std_logic;
   signal notbr : std_logic;
   signal notramcs : std_logic;
   signal ipl : unsigned(2 downto 0);
   signal notoe : std_logic;
   signal notuwe : std_logic;
   signal notlwe : std_logic;
   signal notberr : std_logic;
   signal leds : unsigned(7 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
   constant cpuclock_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: Top PORT MAP (
          clk => clk,
          cpuclock => cpuclock,
          sysreset => sysreset,
          button => button,
          notcpureset => notcpureset,
          notcpuhalt => notcpuhalt,
          notas => notas,
          rnotw => rnotw,
          notuds => notuds,
          notlds => notlds,
          dtack => dtack,
          notbr => notbr,
          notbg => notbg,
          addr => addr,
          data => data,
          notramcs => notramcs,
          ipl => ipl,
          notoe => notoe,
          notuwe => notuwe,
          notlwe => notlwe,
          notberr => notberr,
          leds => leds,
          rx => rx,
          tx => tx
        );

   -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 
   cpuclock_process :process
   begin
		cpuclock <= '0';
		wait for cpuclock_period/2;
		cpuclock <= '1';
		wait for cpuclock_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
