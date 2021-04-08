
# Parameters

    Name :                      causal5_demo-0
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      52029686321 function calls (51868302030 primitive calls) in 57311.36 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57311.358 57311.358 {built-in method builtins.exec}
                      1    1.968    1.968 57311.358 57311.358 <string>:1(<module>)
                      1  165.666  165.666 57309.390 57309.390 main.py:40(teleport)
                5764130   27.274    0.000 17132.301    0.003 agent.py:29(learn)
                2882065   16.345    0.000 15440.512    0.005 game.py:39(step)
                2882065   18.342    0.000 14719.691    0.005 layers.py:581(step)
                5764130  417.621    0.000 14299.196    0.002 learner.py:42(Qlearn)
                2882065  109.485    0.000 10351.739    0.004 agent.py:54(_learn)
                2882065  268.252    0.000 8646.706    0.003 layers.py:17(step)
                2882065 4803.402    0.002 8496.078    0.003 replaybuffer.py:28(teleporter_save_data)
              288206500  673.519    0.000 8350.944    0.000 layer.py:92(move)
        181556705/20173425  730.862    0.000 7060.001    0.000 module.py:715(_call_impl)
                2882065   87.931    0.000 6740.576    0.002 agent.py:115(_learn)
               14409295   35.261    0.000 6564.402    0.000 network.py:24(forward)
               14409295  177.935    0.000 6435.929    0.000 container.py:115(forward)
                2882066  432.769    0.000 6025.345    0.002 layers.py:552(update)
                2882065 3697.661    0.001 5831.176    0.002 agent.py:86(interveen)
                5764130   40.747    0.000 5595.391    0.001 grad_mode.py:23(decorate_context)
                5764130  198.296    0.000 5482.894    0.001 adam.py:55(step)
                2882065 3948.174    0.001 5442.198    0.002 replaybuffer.py:22(sample_data)
              288206500  762.958    0.000 4786.436    0.000 layers.py:598(check)
                5764130 1005.337    0.000 4471.936    0.001 functional.py:53(adam)
                5763100  156.011    0.000 4416.017    0.001 agent.py:49(__call__)
                5764130   36.569    0.000 3479.238    0.001 tensor.py:181(backward)
                5764130   23.910    0.000 3442.668    0.001 __init__.py:68(backward)
                5764130 3269.917    0.001 3269.917    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              279016772 2947.262    0.000 2947.262    0.000 {built-in method clone}
                2882065 1180.772    0.000 2469.059    0.001 agent.py:67(modify)
               28818590   49.437    0.000 2410.484    0.000 conv.py:422(forward)
               28818590   57.927    0.000 2338.101    0.000 conv.py:414(_conv_forward)
               28818590 2268.095    0.000 2268.095    0.000 {built-in method conv2d}
              288206500  520.341    0.000 2259.020    0.000 layers.py:592(isFree)
               37463755   85.255    0.000 2043.514    0.000 linear.py:92(forward)
               25938594 1137.185    0.000 2004.910    0.000 layer.py:163(NoRock_update)
               37463755  139.750    0.000 1913.439    0.000 functional.py:1669(linear)
             2582251273 1441.198    0.000 1738.678    0.000 layer.py:89(isFree)
              800977728  466.603    0.000 1655.801    0.000 {built-in method builtins.any}
                3113614   39.591    0.000 1529.453    0.000 layers.py:602(restart)
               25937555 1466.057    0.000 1466.057    0.000 {built-in method cat}
              363140244  889.155    0.000 1444.951    0.000 tensor.py:933(grad)
             5764932663  969.392    0.000 1402.244    0.000 enum.py:646(__hash__)
                2882065   47.427    0.000 1390.564    0.000 agent.py:110(__call__)
               37463755 1357.940    0.000 1357.940    0.000 {built-in method addmm}
                8645165   64.351    0.000 1343.076    0.000 agent.py:59(modify_board)
                2882065   58.813    0.000 1252.467    0.000 replaybuffer.py:18(stacker)
                3113614   20.304    0.000 1240.505    0.000 level.py:8(__init__)
                5764130  110.823    0.000 1227.486    0.000 optimizer.py:167(zero_grad)
                3113614   50.007    0.000 1069.986    0.000 levels.py:249(generate)
               12436041 1034.961    0.000 1034.961    0.000 {built-in method tensor}
               20237711  182.708    0.000  965.625    0.000 level.py:41(notUsed)
             2850929860  748.178    0.000  906.735    0.000 layers.py:563(<genexpr>)
              103754340  897.053    0.000  897.053    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51873050   45.704    0.000  888.150    0.000 activation.py:713(forward)
                8645165  872.104    0.000  872.104    0.000 {built-in method torch._C._nn.one_hot}
              288206500  541.543    0.000  855.254    0.000 layers.py:369(check)
               51873050   71.502    0.000  842.446    0.000 functional.py:1292(leaky_relu)
                5764130   10.720    0.000  828.062    0.000 game.py:35(board)
              288206500  526.995    0.000  813.459    0.000 layers.py:343(check)
              287661937  795.245    0.000  795.245    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              288206500  504.466    0.000  789.655    0.000 layers.py:381(check)
              302618643  122.027    0.000  770.583    0.000 {built-in method builtins.all}
               51873050  763.761    0.000  763.761    0.000 {built-in method torch._C._nn.leaky_relu}
              288206500  475.451    0.000  757.256    0.000 layers.py:331(check)
              466892726  246.548    0.000  744.367    0.000 overrides.py:1070(has_torch_function)
              103754340  736.849    0.000  736.849    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1228071809  330.783    0.000  673.053    0.000 layers.py:558(<genexpr>)
               14412043   77.292    0.000  628.726    0.000 tensor.py:21(wrapped)
             6107972804  570.020    0.000  570.020    0.000 layer.py:85(positions)
              841757147  555.813    0.000  555.813    0.000 layer.py:142(elements)
                2882065  309.009    0.000  532.033    0.000 collector.py:53(collect)
               51877170  517.722    0.000  517.722    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               51877170  492.517    0.000  492.517    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5763100  166.296    0.000  473.016    0.000 exploration.py:53(softmaxer)
             5764953798  432.856    0.000  432.856    0.000 {built-in method builtins.hash}
               51877170  427.081    0.000  427.081    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               20237711   15.479    0.000  423.437    0.000 level.py:38(elementsIn)
              288206500  254.643    0.000  379.883    0.000 layers.py:320(check)
               51877170  379.581    0.000  379.581    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              288206500  231.656    0.000  356.318    0.000 layers.py:358(check)
                5764130   10.434    0.000  323.467    0.000 loss.py:445(forward)
                5764130   37.814    0.000  313.034    0.000 functional.py:2637(mse_loss)
        3037193443/3037193441  207.509    0.000  288.390    0.000 {built-in method builtins.len}
               51877170  279.635    0.000  279.635    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              985660674  224.249    0.000  278.312    0.000 overrides.py:1083(<genexpr>)
               20237711  134.914    0.000  267.135    0.000 level.py:39(<listcomp>)
             2582251273  248.620    0.000  248.620    0.000 layer.py:199(isBlocking)
              396475832  179.110    0.000  247.872    0.000 layer.py:126(add)
               37463755  247.769    0.000  247.769    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2883217  240.518    0.000  240.518    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               28022526   26.161    0.000  240.098    0.000 layer.py:64(restart)
              289149770  160.336    0.000  237.630    0.000 layer.py:122(remove)
                2882065   87.879    0.000  236.335    0.000 random.py:315(sample)
              954480981  232.343    0.000  232.343    0.000 level.py:32(inverse)
               17292390  218.065    0.000  218.065    0.000 {built-in method sum}
                8646195   43.549    0.000  194.578    0.000 tensor.py:506(__rsub__)
                2882065   15.756    0.000  186.722    0.000 exploration.py:47(epsilonGreedy)
                5764130  179.502    0.000  179.502    0.000 {built-in method torch._C._nn.mse_loss}
                8646195  171.486    0.000  171.486    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                5764994  167.450    0.000  167.450    0.000 {built-in method max}
                3113714   82.572    0.000  163.710    0.000 layers.py:30(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9497199: <causal5_demo_0> in cluster <dcc> Done

Job <causal5_demo_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr  6 23:22:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 23:22:03 2021
Terminated at Wed Apr  7 15:17:19 2021
Results reported at Wed Apr  7 15:17:19 2021

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

    CPU time :                                   57164.83 sec.
    Max Memory :                                 2809 MB
    Average Memory :                             2804.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13575.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57429 sec.
    Turnaround time :                            151664 sec.

The output (if any) is above this job summary.

