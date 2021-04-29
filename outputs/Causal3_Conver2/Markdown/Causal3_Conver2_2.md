
# Parameters

    Name :                      Causal3_Conver2-2
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61363408252 function calls (61043776653 primitive calls) in 86109.28 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.283 86109.283 {built-in method builtins.exec}
                      1    4.520    4.520 86109.283 86109.283 <string>:1(<module>)
                      1  422.642  422.642 86104.762 86104.762 main.py:79(CFagent)
                9996087   42.878    0.000 25044.820    0.003 agent.py:29(learn)
                9996085  642.617    0.000 20254.943    0.002 learner.py:42(Qlearn)
                3332029   17.761    0.000 17630.128    0.005 game.py:41(step)
                3332029   21.879    0.000 16892.836    0.005 layers.py:718(step)
        357372495/37742587 1469.621    0.000 11828.133    0.000 module.py:866(_call_impl)
               27746502   78.080    0.000 11043.760    0.000 network.py:27(forward)
               27746502  373.456    0.000 10778.940    0.000 container.py:117(forward)
                3332029  322.068    0.000 10413.433    0.003 layers.py:17(step)
              333164253  550.889    0.000 10058.449    0.000 layer.py:98(move)
                3332029  391.942    0.000 9752.683    0.003 agent.py:54(_learn)
                3332029  967.755    0.000 9506.799    0.003 agent.py:212(counterfact)
                3332029  387.992    0.000 8885.529    0.003 agent.py:204(_learn)
                3332029 7057.535    0.002 8170.597    0.002 replaybuffer.py:22(sample_data)
                9996085   91.894    0.000 7842.337    0.001 optimizer.py:84(wrapper)
                3332029 6774.242    0.002 7834.794    0.002 replaybuffer.py:67(sample_data)
                9996085   48.646    0.000 7445.278    0.001 grad_mode.py:24(decorate_context)
                9996085  321.101    0.000 7289.952    0.001 adam.py:55(step)
                9996085 1525.135    0.000 6619.993    0.001 _functional.py:53(adam)
                3332030  497.663    0.000 6422.225    0.002 layers.py:684(update)
                3332029  110.155    0.000 6341.643    0.002 agent.py:117(_learn)
                3332029 3479.385    0.001 5911.538    0.002 replaybuffer.py:28(teleporter_save_data)
                8873985  258.834    0.000 5860.730    0.001 agent.py:49(__call__)
              333164253 1197.873    0.000 5784.424    0.000 layers.py:735(check)
                9996085   42.411    0.000 5316.876    0.001 tensor.py:195(backward)
                9996085   45.041    0.000 5273.050    0.001 __init__.py:68(backward)
                3332029 2954.177    0.001 5109.830    0.002 agent.py:88(interveen)
                9996085 5018.198    0.001 5018.198    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               47620428 4269.139    0.000 4269.139    0.000 {built-in method tensor}
               39950970   26.783    0.000 4074.848    0.000 game.py:37(board)
               55493004  127.214    0.000 3987.319    0.000 conv.py:398(forward)
               53312472 2165.463    0.000 3827.282    0.000 layer.py:167(NoRock_update)
               55493004   83.660    0.000 3798.196    0.000 conv.py:390(_conv_forward)
               55493004 3714.536    0.000 3714.536    0.000 {built-in method conv2d}
              333164253  568.294    0.000 3173.838    0.000 layers.py:729(isFree)
                2212376   45.761    0.000 3046.852    0.001 agent.py:176(choose_action)
               76575448  148.147    0.000 3035.665    0.000 linear.py:93(forward)
               76575448   61.888    0.000 2804.162    0.000 functional.py:1737(linear)
               76575448 2727.809    0.000 2727.809    0.000 {built-in method torch._C._nn.linear}
             2451941712 2203.557    0.000 2605.544    0.000 layer.py:95(isFree)
                3332029 1705.382    0.001 2564.331    0.001 agent.py:67(modify)
              234076613 2310.492    0.000 2310.492    0.000 {built-in method clone}
               45526294 1794.138    0.000 1794.138    0.000 {built-in method cat}
               12206014   79.002    0.000 1637.548    0.000 agent.py:59(modify_board)
              104321950   87.000    0.000 1608.275    0.000 activation.py:713(forward)
                3332027   66.660    0.000 1535.879    0.000 agent.py:172(__call__)
              104321950   87.255    0.000 1521.274    0.000 functional.py:1364(leaky_relu)
                4418304   52.155    0.000 1486.399    0.000 layers.py:740(restart)
                3332029 1130.496    0.000 1448.696    0.000 replaybuffer.py:73(CF_save_data)
                3332029   64.905    0.000 1432.876    0.000 agent.py:112(__call__)
              104321950 1417.181    0.000 1417.181    0.000 {built-in method torch._C._nn.leaky_relu}
             4973947603  922.751    0.000 1306.187    0.000 enum.py:646(__hash__)
              333164253  845.340    0.000 1299.306    0.000 layers.py:286(check)
              186593584 1289.030    0.000 1289.030    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              332116726  295.139    0.000 1258.616    0.000 {built-in method builtins.any}
              186593584 1150.979    0.000 1150.979    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9996085  204.933    0.000 1145.733    0.000 optimizer.py:189(zero_grad)
              333164253  657.303    0.000 1110.489    0.000 layers.py:246(check)
               12206014 1087.872    0.000 1087.872    0.000 {built-in method torch._C._nn.one_hot}
              333203000  142.045    0.000 1064.927    0.000 {built-in method builtins.all}
                4418304   27.835    0.000 1047.873    0.000 level.py:8(__init__)
             1191783176 1006.230    0.000 1006.230    0.000 layer.py:146(elements)
             1544554353  438.912    0.000  964.434    0.000 layers.py:690(<genexpr>)
             2959062264  796.655    0.000  963.477    0.000 layers.py:700(<genexpr>)
                3332029   72.343    0.000  845.687    0.000 replaybuffer.py:18(stacker)
                4418304   95.462    0.000  809.794    0.000 levels.py:164(generate)
                3332027   69.616    0.000  806.722    0.000 replaybuffer.py:63(stacker)
               93296792  753.255    0.000  753.255    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               93296792  662.837    0.000  662.837    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93296792  608.226    0.000  608.226    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15500666  234.540    0.000  603.032    0.000 random.py:315(sample)
               93296792  602.471    0.000  602.471    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8873985  217.868    0.000  598.115    0.000 exploration.py:53(softmaxer)
             6347639068  589.468    0.000  589.468    0.000 layer.py:91(positions)
                8836608   85.023    0.000  584.009    0.000 level.py:41(notUsed)
                2212376  518.226    0.000  583.024    0.000 agent.py:187(convert_values)
        7548220711/7548220708  518.072    0.000  581.085    0.000 {built-in method builtins.len}
              333164253  342.184    0.000  550.562    0.000 layers.py:313(check)
              653077628  429.278    0.000  538.735    0.000 tensor.py:906(grad)
              333164253  346.144    0.000  536.427    0.000 layers.py:273(check)
                3332029  298.289    0.000  508.092    0.000 collector.py:46(collect)
              249614654  493.562    0.000  493.562    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9996085   17.349    0.000  462.609    0.000 loss.py:527(forward)
              333164253  312.015    0.000  455.970    0.000 layers.py:48(check)
               93296792  455.318    0.000  455.318    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9996085   46.258    0.000  445.260    0.000 functional.py:2898(mse_loss)
             4973985602  383.443    0.000  383.443    0.000 {built-in method builtins.hash}
               35346432   47.631    0.000  374.137    0.000 layer.py:69(restart)
              333164253  240.121    0.000  359.613    0.000 layers.py:23(check)
              178534129  230.245    0.000  337.169    0.000 layers.py:113(isDone)
              544511219  237.158    0.000  326.073    0.000 layer.py:130(add)
              451161030  215.334    0.000  313.892    0.000 random.py:250(_randbelow_with_getrandbits)
              321024455  199.097    0.000  291.802    0.000 layer.py:126(remove)
                6664060  273.419    0.000  273.419    0.000 {built-in method nonzero}
                9996085  267.874    0.000  267.874    0.000 {built-in method torch._C._nn.mse_loss}
               55493004   40.657    0.000  260.768    0.000 flatten.py:39(forward)
             3022173802  245.861    0.000  245.861    0.000 {method 'random' of '_random.Random' objects}
                9997305  241.281    0.000  241.281    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579159: <Causal3_Conver2_2> in cluster <dcc> Done

Job <Causal3_Conver2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 05:58:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 05:58:16 2021
Terminated at Wed Apr 28 05:53:32 2021
Results reported at Wed Apr 28 05:53:32 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85902.45 sec.
    Max Memory :                                 9136 MB
    Average Memory :                             6075.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7248.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86118 sec.
    Turnaround time :                            97766 sec.

The output (if any) is above this job summary.

