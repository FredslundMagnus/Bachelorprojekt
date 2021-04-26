
# Parameters

    Name :                      Causal4_Cf_convert4_TopN3-0
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      77913519983 function calls (77560465660 primitive calls) in 86121.64 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.640 86121.640 {built-in method builtins.exec}
                      1    3.889    3.889 86121.640 86121.640 <string>:1(<module>)
                      1  353.534  353.534 86117.751 86117.751 main.py:79(CFagent)
               11515989   42.036    0.000 27542.961    0.002 agent.py:29(learn)
               11515988  689.801    0.000 22593.449    0.002 learner.py:42(Qlearn)
                3838663   14.872    0.000 22477.711    0.006 game.py:41(step)
                3838663   20.584    0.000 21620.320    0.006 layers.py:718(step)
                3838663  351.885    0.000 14832.475    0.004 layers.py:17(step)
              383547869 1108.461    0.000 14447.702    0.000 layer.py:98(move)
        395269227/42216595 1550.021    0.000 12490.095    0.000 module.py:866(_call_impl)
               30700607   83.254    0.000 11668.501    0.000 network.py:27(forward)
               30700607  385.163    0.000 11394.122    0.000 container.py:117(forward)
                3838663  870.274    0.000 10717.878    0.003 agent.py:210(counterfact)
                3838663  346.766    0.000 10668.708    0.003 agent.py:54(_learn)
                3838663  342.924    0.000 9808.269    0.003 agent.py:202(_learn)
              383547869 1852.262    0.000 9215.049    0.000 layers.py:735(check)
               11515988   96.570    0.000 8982.431    0.001 optimizer.py:84(wrapper)
               11515988   48.309    0.000 8552.969    0.001 grad_mode.py:24(decorate_context)
               11515988  334.715    0.000 8390.508    0.001 adam.py:55(step)
               11515988 1756.317    0.000 7667.999    0.001 _functional.py:53(adam)
                3838663  103.981    0.000 7000.339    0.002 agent.py:117(_learn)
                3838664  550.865    0.000 6738.388    0.002 layers.py:684(update)
               60310020 6024.912    0.000 6024.912    0.000 {built-in method tensor}
                9579308  206.895    0.000 5956.100    0.001 agent.py:49(__call__)
               11515988   56.170    0.000 5821.152    0.001 tensor.py:195(backward)
               51523101   30.362    0.000 5818.278    0.000 game.py:37(board)
               11515988   44.725    0.000 5763.419    0.001 __init__.py:68(backward)
                3838663 4616.327    0.001 5701.262    0.001 replaybuffer.py:22(sample_data)
                3838663 4476.838    0.001 5544.991    0.001 replaybuffer.py:67(sample_data)
               11515988 5498.010    0.000 5498.010    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               76773270 2619.604    0.000 4602.809    0.000 layer.py:151(update)
               61401214  137.073    0.000 4188.654    0.000 conv.py:398(forward)
               61401214   79.480    0.000 3989.267    0.000 conv.py:390(_conv_forward)
                3838663 1592.591    0.000 3950.890    0.001 agent.py:88(interveen)
               61401214 3909.787    0.000 3909.787    0.000 {built-in method conv2d}
              383547869  670.772    0.000 3394.541    0.000 layers.py:729(isFree)
               84424495  167.769    0.000 3230.682    0.000 linear.py:93(forward)
                3838663 1704.516    0.000 3083.357    0.001 replaybuffer.py:28(teleporter_save_data)
               84424495   68.221    0.000 2978.673    0.000 functional.py:1737(linear)
               84424495 2893.486    0.000 2893.486    0.000 {built-in method torch._C._nn.linear}
                3838663 1794.908    0.000 2727.253    0.001 agent.py:67(modify)
             3218864648 2228.967    0.000 2723.768    0.000 layer.py:95(isFree)
                1927986   40.430    0.000 2550.372    0.001 agent.py:175(choose_action)
             7153641822 1298.099    0.000 1848.051    0.000 enum.py:646(__hash__)
               51804596 1778.563    0.000 1778.563    0.000 {built-in method cat}
               13417971   91.705    0.000 1705.013    0.000 agent.py:59(modify_board)
              115125102   94.262    0.000 1699.283    0.000 activation.py:713(forward)
              384173905  385.680    0.000 1664.002    0.000 {built-in method builtins.any}
                3838662   55.038    0.000 1655.774    0.000 agent.py:171(__call__)
              115125102   96.310    0.000 1605.021    0.000 functional.py:1364(leaky_relu)
                3838663   54.812    0.000 1562.012    0.000 agent.py:112(__call__)
              115125102 1490.428    0.000 1490.428    0.000 {built-in method torch._C._nn.leaky_relu}
              214965108 1476.018    0.000 1476.018    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              383547869 1102.481    0.000 1454.918    0.000 layers.py:77(check)
              139648676 1400.304    0.000 1400.304    0.000 {built-in method clone}
               11515988  245.825    0.000 1343.752    0.000 optimizer.py:189(zero_grad)
              214965108 1318.429    0.000 1318.429    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              383547869  849.729    0.000 1308.390    0.000 layers.py:286(check)
                3531159   41.382    0.000 1293.313    0.000 layers.py:740(restart)
             4183687651 1050.229    0.000 1278.322    0.000 layers.py:700(<genexpr>)
                3838663  974.541    0.000 1235.549    0.000 replaybuffer.py:73(CF_save_data)
              383547869  738.319    0.000 1206.265    0.000 layers.py:246(check)
               13417971 1109.292    0.000 1109.292    0.000 {built-in method torch._C._nn.one_hot}
             1241169085 1091.981    0.000 1091.981    0.000 layer.py:146(elements)
              107482554  938.701    0.000  938.701    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3531159   19.693    0.000  916.949    0.000 level.py:8(__init__)
             9215995073  834.998    0.000  834.998    0.000 layer.py:91(positions)
                3838663   63.965    0.000  810.937    0.000 replaybuffer.py:18(stacker)
                3838662   67.952    0.000  799.734    0.000 replaybuffer.py:63(stacker)
              383547869  579.679    0.000  762.943    0.000 layers.py:62(check)
              107482554  750.052    0.000  750.052    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3531159  118.720    0.000  729.998    0.000 levels.py:199(generate)
        10176248521/10176248518  650.282    0.000  720.723    0.000 {built-in method builtins.len}
              107482554  704.033    0.000  704.033    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              107482554  694.174    0.000  694.174    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              383547869  423.690    0.000  650.100    0.000 layers.py:313(check)
              383547869  405.443    0.000  636.274    0.000 layers.py:273(check)
              752377962  492.846    0.000  612.016    0.000 tensor.py:906(grad)
                9579308  222.213    0.000  592.478    0.000 exploration.py:53(softmaxer)
               14739644  221.770    0.000  584.636    0.000 random.py:315(sample)
                3838663  344.462    0.000  583.163    0.000 collector.py:46(collect)
              383866400  107.167    0.000  569.750    0.000 {built-in method builtins.all}
              383547869  376.197    0.000  550.482    0.000 layers.py:48(check)
             7153685421  549.959    0.000  549.959    0.000 {built-in method builtins.hash}
              107482554  541.062    0.000  541.062    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1049249599  241.966    0.000  508.185    0.000 layers.py:690(<genexpr>)
                7062318   57.733    0.000  495.040    0.000 level.py:41(notUsed)
                1927986  413.912    0.000  487.404    0.000 agent.py:186(convert_values)
               11515988   17.465    0.000  481.318    0.000 loss.py:527(forward)
               11515988   42.674    0.000  463.853    0.000 functional.py:2898(mse_loss)
              383547869  288.855    0.000  416.484    0.000 layers.py:23(check)
             4233777130  340.623    0.000  340.623    0.000 {method 'random' of '_random.Random' objects}
               35311590   48.363    0.000  323.062    0.000 layer.py:69(restart)
              156905309  322.574    0.000  322.574    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              333491863  226.507    0.000  314.093    0.000 layer.py:126(remove)
              544570445  220.797    0.000  303.286    0.000 layer.py:130(add)
              456470256  201.975    0.000  294.718    0.000 random.py:250(_randbelow_with_getrandbits)
               11515988  287.688    0.000  287.688    0.000 {built-in method torch._C._nn.mse_loss}
               76773270  284.863    0.000  284.863    0.000 layer.py:163(<listcomp>)
                7677328  280.237    0.000  280.237    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551818: <Causal4_Cf_convert4_TopN3_0> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 05:48:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 05:48:51 2021
Terminated at Sat Apr 24 05:44:24 2021
Results reported at Sat Apr 24 05:44:24 2021

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

    CPU time :                                   86043.21 sec.
    Max Memory :                                 3437 MB
    Average Memory :                             3405.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12947.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86132 sec.
    Turnaround time :                            267832 sec.

The output (if any) is above this job summary.

