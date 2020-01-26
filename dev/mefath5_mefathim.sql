-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 26, 2020 at 08:37 AM
-- Server version: 10.2.27-MariaDB-log
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mefath5_mefathim`
--

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `sid` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL,
  `create_time` datetime NOT NULL DEFAULT current_timestamp(),
  `update_time` datetime DEFAULT NULL,
  `ip_address` varchar(20) NOT NULL,
  `user_agent` varchar(256) NOT NULL,
  `logged_out` tinyint(1) NOT NULL DEFAULT 0,
  `logout_time` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `email` varchar(64) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `middle_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) NOT NULL,
  `status` int(3) NOT NULL DEFAULT 1,
  `nickname` varchar(64) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `creation_date` date NOT NULL,
  `gender` int(3) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `country` varchar(3) DEFAULT NULL,
  `phone_number` varchar(30) DEFAULT NULL,
  `picture_number` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `first_name`, `middle_name`, `last_name`, `status`, `nickname`, `password_hash`, `salt`, `creation_date`, `gender`, `date_of_birth`, `city`, `country`, `phone_number`, `picture_number`) VALUES
(1, 'ofni.fresh@gmail.com', 'יצחק', '', '', 0, 'סאטמער', '4f5cb4845d27637f1fc5e8b6426a087f4e271546', '7381', '2019-12-16', 1, '0000-00-00', '', '', '', 7),
(2, '7142205@gmail.com', '', '', '', 0, 'אברמי', 'c2df941b7325f62890541018c79fb86d8acce4a2', '7G1rl', '2019-12-16', 1, '0000-00-00', '', 'isr', '', 11),
(4, 'nbasa02@gmail.com', 'נהוראי', '', 'בסה', 0, 'גישמק', 'd4697da3230bde9788e3efbc2dc35b1f0097019d', '1231', '2019-12-17', 1, '2019-12-17', 'אלקנה', 'isr', '0526201011', 7),
(6, 'chsh32340@gmail.com', 'חנוך', '', 'שיינר', 0, 'חנוך', 'd075603c07dceec08b097ac09a297e84e155b99c', '5502', '2019-12-17', 1, '1994-11-11', 'בני ברק', 'isr', '1234567890', 2),
(8, 'ronavital999@gmail.com', 'ron', '', 'avital', 0, 'ron', '5cab87774b0425251c23d8c887a0fd74ad9d2017', '2184', '2019-12-17', 1, '2019-12-17', 'Bnei Brak', 'ישר', '0549983018', NULL),
(10, 'eichlermosh@gmail.com', 'משה', 'יוסף', 'אייכלר', 0, 'מושקה', 'e88f1d53d36112c835e25284ff2dd2e27f6239e8', '8081', '2019-12-17', 1, '2019-12-17', 'ירושלים', 'isr', '0548597760', NULL),
(11, 'meirbr88@gmail.com', 'מאיר', 'מאיר', 'ברסלואר', 0, 'מאיר', '73fb5f8d7cfd2120cd1c95df8807df8da42a4f44', '4547', '2019-12-17', 1, '2019-12-17', 'פתח תקווה', 'isr', '0587160468', NULL),
(12, 'yp131323@gmail.com', 'יעקב', '', 'פרייזלר', 0, 'יענקי', '8e93c3adef25a74542018f6e7a45581038e61bc1', '9ERgp', '2019-12-17', 1, '1997-08-26', 'בני ברק', 'isr', '', 4),
(14, 'yishayish@gmail.com', 'ישי', 'משה', 'שטרסלר', 0, 'ישי', '5e6e681d465c8b2d4bdfec8e095276e38e4a2b54', '8808', '2019-12-18', 1, '1987-01-16', 'בית שמש', 'ישר', '0548416385', NULL),
(17, 'ben8652800@gmail.com', 'ben', 'zion', 'katz', 0, 'בנצי', 'cbce00b1b1ace7e21bf77ed9457bb950b3628cf7', '8099', '2019-12-23', 1, '1989-05-31', 'ashdod', 'ישר', '0504166992', NULL),
(19, 'ilan@zisser.com', 'אילן', '', 'זיסר', 0, 'אילן אלכס', 'd7e93030c6452ca7951ed75eca1151a77fdb0f89', '5699', '2019-12-25', 1, '1964-07-25', 'תל אביב', 'isr', '0544985726', 11),
(20, 'bentsikalat@gmail.com', 'בנצי', '', 'חלאט', 0, 'קוצו של יוד', '5cd8b381d5c1a2d999f5fc89b27f819a3008508d', '9920', '2019-12-25', 1, '1800-01-22', 'פתח תקווה', 'isr', '0537138979', 6),
(21, 'ytzyk550@gmail.com', '', '', '', 0, 'المطورون', 'aa642e6df802a6586aeb05a7371a8c60c66ec051', 'KRcN2', '2019-12-25', 1, '0000-00-00', '', 'isr', '', 12),
(24, 'pituchimh@gmail.com', 'akiva', '', 'ashtamker', 0, 'akiva', 'd0cc804a7170aafedda93dd68c1fcadb90be98cf', '5959', '2019-12-25', 1, '1990-09-11', 'baitar', 'isr', '0548460963', NULL),
(25, 'y131323@gmail.com', 'None', NULL, 'None', 0, 'יוסי', 'bef38bb31531404fcb18b67f64be6dd5eb724fef', '2363', '2019-12-25', 1, '2019-12-11', 'None', 'isr', 'None', NULL),
(28, 'batelcohen123@gmail.com', 'יוסי', 'שלום', 'וינשטוק', 0, 'nbasa', '7a479588377c843fd4957ba02bf050842c77b8bf', '6213', '2019-12-30', 1, '2019-12-30', 'bet shemesh', 'ישר', '0548187150', NULL),
(32, 'example@gmail.com', 'דוגמה', NULL, 'None', 0, 'דוגמה', 'd3988e677e8663d56d534838f4e48205e71b6e23', '5775', '2019-12-30', 1, '2019-12-30', 'None', 'isr', 'None', NULL),
(33, 'yosi.vaynshtok@gmail.com', 'יוסי', '', 'וינשטוק', 0, 'yossi', 'e83f4d52d0053acb5d80766224e943582a4ab9aa', '8872', '2019-12-31', 1, '1987-02-27', 'None', 'isr', 'None', 3),
(35, 'yossi.vaynshtok@gmail.com', 'יוסי', NULL, 'וינשטוק', 0, 'yossi', '1ae4b3cbdb9a8b8f1de82aee25b41e20bdcdb94f', '2076', '2019-12-31', 1, '1987-02-27', 'בית שמש', 'isr', '0527161609', NULL),
(38, 'melijurko@gmail.com', 'avraham', '', 'jurkowicz', 0, 'אלקי אברהם', 'ca91f797ed0bf6bc620dcce8c839497c47960b3a', '9749', '2019-12-31', 1, '2020-01-01', 'בני ברק', 'isr', 'None', 4),
(41, 'eichler@gmail.com', 'משה', 'יוסף', 'אייכלר', 0, 'מושקה', 'c4cd86f2626326bbe58dedce77e27504051f4cfd', '6191', '2020-01-01', 1, '1111-11-11', 'ירושלים', 'isr', '0548597760', NULL),
(42, 'benzimraaa@gmail.com', 'אברהם', '', 'בן זימרא', 0, 'אברהם', 'fb949364f04e0b32ea4e3c546e484c45a8eb6999', '4143', '2020-01-01', 1, '1995-10-27', 'ירושלים', 'isr', '0527644632', NULL),
(43, 'sshtern@gmail.com', 'שמואל', '', 'שטרן', 0, 'אברמי', 'ad3261a25fd344cb49a818a6be5c871a2e5e0bd1', '7988', '2020-01-01', 1, '2020-01-03', 'בני ברק', 'isr', '0533258888', NULL),
(45, 'eichlermoshe@gmail.com', 'משה', '', '', 0, 'Donald Trump', '84fb40309324cfb7ce81f8bf92e0c5f64b39fae7', '1055', '2020-01-01', 1, '0000-00-00', '', 'isr', '', NULL),
(46, 'meirb88@gmail.com', 'מאיר', NULL, 'ברסלואר', 0, 'מאירקה', 'c62d4d28c11174e9154f891a1d30d35c2551bcd4', '8150', '2020-01-01', 3, '1998-01-20', 'פתח תקוה', 'isr', '0587160468', NULL),
(47, 'ytr@ytr', 'try', NULL, 'None', 0, 'None', '590ea50c126876d16f0389159c58f8f306431324', '7105', '2020-01-05', 1, '1111-11-11', 'None', 'isr', 'None', NULL),
(49, 'poiu@poiu', 'יעקב', NULL, 'None', 0, 'None', '5049015b212d095c02a0750ee88ab4dfa7d226d2', '4875', '2020-01-05', 1, '2000-02-02', 'None', 'isr', 'None', NULL),
(50, '123@123', 'יענקי', '', '', 0, 'חמוצים', 'cc3f2f14ea31cc7d97318059c7ee547772a10f2f', '7106', '2020-01-06', 3, '0000-00-00', 'ירושלים', 'isr', '12345678', 7),
(51, '1234@1234', 'nav', '', 'None', 0, 'None', 'fa1585ff383963ac0a0f8aadf502bdd85b51475f', '3168', '2020-01-06', 1, '1111-11-11', 'None', 'isr', 'None', NULL),
(54, '12345@12345', 'nav', '', 'None', 0, 'nav', '0230407c035835472c92a8a34031ebff621406d7', '1796', '2020-01-06', 1, '1111-11-11', 'None', 'isr', 'None', NULL),
(55, 'alert@a', 'haker', '', 'None', 0, 'דוגמה', 'f614c384cedc5bf3256c574155584839c3a607c7', '2385', '2020-01-06', 1, '1111-11-11', 'None', 'isr', 'None', NULL),
(56, 'ytzyk@gmail.com', 'u', '', 'y', 0, 'האקר', '712523b6b8c4010d1cb6c6cfd22d0801590e8265', '6149', '2020-01-08', 1, '0005-05-05', 'ירושלים', 'isr', '0533258888', NULL),
(57, 'a0525608687@gmail.com', 'adiel', NULL, 'barzel', 0, 'AdielBarzel', '7cbf10cead975d152b6e46c538b1aa8d0c8023d4', '7341', '2020-01-11', 1, '1987-02-22', 'imanuel', 'Isr', '0534215437', NULL),
(58, '1@1', 'נחמן', NULL, 'מאומן', 0, 'נח נח', 'd2464b59a6acaa561961a4ad72ae63fb13b8adaa', '3286', '2020-01-11', 1, '1111-11-11', 'אומן', 'ukr', '111111111', NULL),
(59, '123@12', 'בנימין', '', 'נתניהו', 0, 'יענקי', '24a523abc64bb2e2684a5c4a7e0961791efa4b80', '8698', '2020-01-11', 1, '1111-11-11', 'ירושלים', 'isr', '123456789', NULL),
(60, 'urko@gmail.com', 'חנהלה', NULL, 'None', 0, 'חנהלה', '401127fc67636d207de492d086c74c85aad2ac0a', '4326', '2020-01-13', 1, '1567-03-01', 'bet shemesh', 'Isr', '0548187150', NULL),
(61, '7242205@gmail.com', 'אברהם', NULL, 'לוינגר', 0, 'שלום 1', 'b2239447bf69707dd60a064bf7c94c3f7af5c031', '4037', '2020-01-13', 1, '0000-00-00', 'None', 'isr', 'None', NULL),
(62, 'oz91342@gmail.com', 'עוז', NULL, 'כהן', 0, 'עוז', 'ffba02b2a74dee388a3bbb34626e9e8f0028b55b', '8606', '2020-01-21', 1, '1992-10-24', 'ירושלים', 'isr', '0525716313', NULL),
(63, 'bentsikhalat@gmail.com', '1', NULL, 'None', 0, '1', '8655e6639a4dcd20cd76d5b4035a068add9f36ae', '3150', '2020-01-26', 1, '0111-11-11', 'תל אביב', 'isr', '1111111111', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD KEY `update_time` (`update_time`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;
COMMIT;


--
-- מבנה טבלה עבור טבלה `posts`
--

CREATE TABLE `posts` (
  `post_id` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `post_text` text NOT NULL,
  `back_color` varchar(30) NOT NULL,
  `text_color` varchar(30) NOT NULL,
  `font_type` varchar(30) NOT NULL,
  `font_size` varchar(30) NOT NULL,
  `write_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- אינדקסים לטבלה `posts`
--
ALTER TABLE `posts`
  ADD KEY `id` (`post_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
